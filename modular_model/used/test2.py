import ModularTask
#---------------------------------
#     General Setting
#---------------------------------
component = ['Oxygen','Nitrogen']
units = {'T':'℃',
         'P':'kPa',
         'F':'kmol'}
testTask2 = ModularTask.PyomoTask('test_model2',component,units)
options = {
            'ConnectionMode': 'CombinedMode' #IsolatedMode
        }
testTask2.setModelingOption(options)
#---------------------------------
#        System Parts
#---------------------------------
compositionThermo = ModularTask.Thermodynamics.SimpleFittingComposition(testTask2)
hydraulics = ModularTask.Hydraulics.defaultMethod(testTask2)
vap_enthalpy = ModularTask.Thermodynamics.SimpleFittingVaporEnthalpy(testTask2)
liq_enthalpy = ModularTask.Thermodynamics.SimpleFittingLiquidEnthalpy(testTask2)
bubble_point = ModularTask.Thermodynamics.SimpleFittingBubblePoint(testTask2)
#---------------------------------
#        Feed
#---------------------------------
testTask2.addDevice('TwoPhaseStream','Feed')
options = {
    'CompositionThermo' : compositionThermo,
    'VaporEnthalpy':vap_enthalpy,
    'LiquidEnthalpy': liq_enthalpy
}
testTask2.devices['Feed'].setModelingOption(options)
specifications = {
            'MolarFlow':2000,
            'ComponentComposition':{'Oxygen':0.21,'Nitrogen':0.79},
            'Pressure':564,
            'VaporFraction':0.8
}
testTask2.devices['Feed'].setSpecificaitons(specifications)
#---------------------------------
#          Column
#---------------------------------
testTask2.addDevice('ColumnBody','Column')
testTask2.devices['Column'].setTrayInfo(10,{1:'TwoPhaseFeed'},extractions=None)
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
    'PressureProfile' : 'SimpleLinear'
}
testTask2.devices['Column'].setModelingOption(options)
specifications = {
    'TopTrayPressure':539.56,
    'BottomTrayPressure':564
}
testTask2.devices['Column'].setSpecificaitons(specifications)
weights= {
            'FlowEquWeight':1e-3,
            'EnthalpyEquWeight':1e-5,
            'PressureEquWeight':1e-2
}
testTask2.devices['Column'].setConstraintWeight(weights)
#---------------------------------
#          Condensor
#---------------------------------
testTask2.addDevice('NaiveTotalCondensor','Condensor')
options = {
    'BubblePoint': bubble_point,
    'LiquidEnthalpy': liq_enthalpy,
    'Pressure' : 'SameWithInlet'
}
testTask2.devices['Condensor'].setModelingOption(options)
specifications = {
    'RefluxRatio':0.38,
}
testTask2.devices['Condensor'].setSpecificaitons(specifications)
weights= {
            'FlowEquWeight':1e-3,
            'EnthalpyEquWeight':1e-5
}
testTask2.devices['Condensor'].setConstraintWeight(weights)
#---------------------------------
#       Condensor Heat
#---------------------------------
testTask2.addDevice('HeatStream','CndsHeat')
specifications = {
    'Temperature':-186,
    'HeatFlow':1.07e7
}
testTask2.devices['CndsHeat'].setSpecificaitons(specifications)
#---------------------------------
#          Connections
#---------------------------------
connections = [['Feed','Outlet','Column','Feed1'],
               ['Column','ToCondensor','Condensor','Inlet'],
               ['Condensor', 'Reflux','Column', 'Reflux']]
testTask2.addConnections(connections)
#---------------------------------
#          Pyomo
#---------------------------------
testTask2.generatePyomoModel("pyomoModel2.py")

from pyomoModel2 import test_model2
ModularTask.InitValueTemplate.to_csv_template(test_model2, 'InitValueTemplate2.txt')
ModularTask.InitValueTemplate.load_init_from_template(test_model2, 'InitValueFilled2.txt')

from pyomo.environ import *
solver=SolverFactory('ipopt')
results = solver.solve(test_model2,tee=True)
with open('reflux_display.txt', 'w') as file:
    test_model2.display(ostream=file)
