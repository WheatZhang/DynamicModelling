import sys
sys.path.append("../")
import ModularTask
#---------------------------------
#     General Setting
#---------------------------------
component = ['Oxygen','Nitrogen']
units = {'T':'℃',
         'P':'kPa',
         'F':'kmol/h',
         'h':'kJ/kmol'}
testTask = ModularTask.PyomoDynamicTask('test_model',component,units)
options = {
            'ConnectionMode': 'CombinedMode' # or: IsolatedMode
        }
testTask.setModelingOption(options)
testTask.setSimulationTime((0,10), 10)
#---------------------------------
#        System Parts
#---------------------------------
compositionThermo = ModularTask.VLEThermo.SimpleFittingComposition(testTask)
hydraulics = ModularTask.Hydraulics.SimpleHydraulics(testTask)
hydraulics.setParameterValue({"k":10})
vap_enthalpy = ModularTask.EtlpThermo.SimpleFittingVaporEnthalpy(testTask)
liq_enthalpy = ModularTask.EtlpThermo.SimpleFittingLiquidEnthalpy(testTask)
bubble_point = ModularTask.TempPointThermo.SimpleFittingBubblePoint(testTask)
index_reduce_thermo = ModularTask.SpecialThermo.SimpleFitIndexReduRelatedThermo(testTask)
#---------------------------------
#        Feed
#---------------------------------
testTask.addDevice('TwoPhaseStream','Feed')
options = {
    'CompositionThermo' : compositionThermo,
    'VaporEnthalpy':vap_enthalpy,
    'LiquidEnthalpy': liq_enthalpy
}
testTask.devices['Feed'].setModelingOption(options)
specifications = {
            'MolarFlow':2000,
            'ComponentComposition':{'Oxygen':0.21,'Nitrogen':0.79},
            'Pressure':564,
            'VaporFraction':0.8
}
testTask.devices['Feed'].setSpecificaitons(specifications)
#---------------------------------
#          Column Body
#---------------------------------
testTask.addDevice('ColumnBody','Column')
testTask.devices['Column'].setTrayInfo(10,{1:'TwoPhaseFeed'},extractions=None)
options = {
    'TrayEfficiency': False,
    'TrayHeatLeakage' : False,
    'FloodingConstraint' : False,
    'FloodingIndication' : False,
    'SumpLevelControl' : False,
    'CompositionThermo' : compositionThermo,
    'VaporEnthalpy':vap_enthalpy,
    'LiquidEnthalpy': liq_enthalpy,
    'Hydraulics': hydraulics,
    'IndexReduRelatedThermo':index_reduce_thermo,
    'PressureProfile' : 'SimpleLinear'
}
testTask.devices['Column'].setModelingOption(options)
specifications = {
    'TopTrayPressure':539.56,
    'BottomTrayPressure':564
}
testTask.devices['Column'].setSpecificaitons(specifications)
weights= {
            'FlowEquWeight':1e-3,
            'EnthalpyEquWeight':1e-5,
            'PressureEquWeight':1e-2
}
testTask.devices['Column'].setConstraintWeight(weights)
testTask.devices['Column'].setTimeDependParam(['BtmPressure'])
#---------------------------------
#          Column Sump
#---------------------------------
testTask.addDevice('ColumnSump','Sump')
options = {
    'HoldupDensity': 'Constant',
    'LiquidEnthalpy': liq_enthalpy
}
testTask.devices['Sump'].setModelingOption(options)
specifications = {
    'SumpCrossSection' : 6,
    'NominalLiquidDensity' : 1000,
    'ControllerKc' : 1,
    'ControllerTi' : 100,
    'LevelSetpoint' : 0.5
}
testTask.devices['Sump'].setSpecificaitons(specifications)
weights= {
            'FlowEquWeight':1e-3,
}
testTask.devices['Sump'].setConstraintWeight(weights)
#---------------------------------
#          Condensor
#---------------------------------
testTask.addDevice('NaiveTotalCondensor','Condensor')
options = {
    'BubblePoint': bubble_point,
    'LiquidEnthalpy': liq_enthalpy,
    'Pressure' : 'SameWithInlet'
}
testTask.devices['Condensor'].setModelingOption(options)
specifications = {
    'RefluxRatio':0.93,
}
testTask.devices['Condensor'].setSpecificaitons(specifications)
weights= {
            'FlowEquWeight':1e-3,
            'EnthalpyEquWeight':1e-5
}
testTask.devices['Condensor'].setConstraintWeight(weights)
#---------------------------------
#          Reboiler
#---------------------------------
testTask.addDevice('NaiveReboiler','Reboiler')
options = {
    'CompositionThermo' : compositionThermo,
    'VaporEnthalpy':vap_enthalpy,
    'LiquidEnthalpy': liq_enthalpy,
    'Pressure' : 'SameWithInlet',
    'CheckTempDifference': False
}
testTask.devices['Reboiler'].setModelingOption(options)
testTask.devices['Reboiler'].setSpecificaitons({})
weights= {
            'FlowEquWeight':1e-3,
            'EnthalpyEquWeight':1e-5
}
testTask.devices['Reboiler'].setConstraintWeight(weights)
#---------------------------------
#         GN Product
#---------------------------------
testTask.addDevice('NaiveSplitter','GNSplitter')
options = {
    'Mode' : 'OutletARatio'
}
testTask.devices['GNSplitter'].setModelingOption(options)
specifications = {
    'OutletADrawRatio':0.587744831
}
testTask.devices['GNSplitter'].setSpecificaitons(specifications)
weights= {
            'FlowEquWeight':1e-3
}
testTask.devices['GNSplitter'].setConstraintWeight(weights)
#---------------------------------
#          Connections
#---------------------------------
connections = [['Feed','Outlet','Column','Feed1'],
               ['Column','ToCondensor','GNSplitter','Inlet'],
               ['GNSplitter','OutletB','Condensor','Inlet'],
               ['Condensor', 'Reflux','Column', 'Reflux'],
               ['Column','SumpOutlet','Sump','Inlet'],
               ['Sump','Outlet','Reboiler','Inlet'],
               ['Condensor','HeatFlow','Reboiler','HeatFlow']]
testTask.addConnections(connections)
#---------------------------------
#          Pyomo
#---------------------------------
testTask.loadStaticInitValue("StaticInitValue.txt")
testTask.getNaiveDynamicInitValue()
testTask.generatePyomoModel("pyomoDyn.py")

from pyomoDyn import test_model

from pyomo.environ import *
solver=SolverFactory('ipopt')
results = solver.solve(test_model,tee=True)
with open('dynamic_display.txt', 'w') as file:
    test_model.display(ostream=file)