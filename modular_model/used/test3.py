import ModularTask
#---------------------------------
#     General Setting
#---------------------------------
component = ['Oxygen','Nitrogen']
units = {'T':'℃',
         'P':'kPa',
         'F':'kmol'}
testTask3 = ModularTask.PyomoTask('test_model3',component,units)
options = {
            'ConnectionMode': 'CombinedMode' #IsolatedMode
        }
testTask3.setModelingOption(options)
#---------------------------------
#        System Parts
#---------------------------------
compositionThermo = ModularTask.Thermodynamics.SimpleFittingComposition(testTask3)
hydraulics = ModularTask.Hydraulics.defaultMethod(testTask3)
vap_enthalpy = ModularTask.Thermodynamics.SimpleFittingVaporEnthalpy(testTask3)
liq_enthalpy = ModularTask.Thermodynamics.SimpleFittingLiquidEnthalpy(testTask3)
bubble_point = ModularTask.Thermodynamics.SimpleFittingBubblePoint(testTask3)
#---------------------------------
#        Feed
#---------------------------------
testTask3.addDevice('TwoPhaseStream','Feed')
options = {
    'CompositionThermo' : compositionThermo,
    'VaporEnthalpy':vap_enthalpy,
    'LiquidEnthalpy': liq_enthalpy
}
testTask3.devices['Feed'].setModelingOption(options)
specifications = {
            'MolarFlow':2000,
            'ComponentComposition':{'Oxygen':0.21,'Nitrogen':0.79},
            'Pressure':564,
            'VaporFraction':0.8
}
testTask3.devices['Feed'].setSpecificaitons(specifications)
#---------------------------------
#          Column
#---------------------------------
testTask3.addDevice('ColumnBody','Column')
testTask3.devices['Column'].setTrayInfo(10,{1:'TwoPhaseFeed'},extractions=None)
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
testTask3.devices['Column'].setModelingOption(options)
specifications = {
    'TopTrayPressure':539.56,
    'BottomTrayPressure':564
}
testTask3.devices['Column'].setSpecificaitons(specifications)
weights= {
            'FlowEquWeight':1e-3,
            'EnthalpyEquWeight':1e-5,
            'PressureEquWeight':1e-2
}
testTask3.devices['Column'].setConstraintWeight(weights)
#---------------------------------
#          RefFlow
#---------------------------------
testTask3.addDevice('LiquidStream','RefFlow')
options = {
    'LiquidEnthalpy': liq_enthalpy
}
testTask3.devices['RefFlow'].setModelingOption(options)
specifications = {
            'MolarFlow':586.5629703759538,
            'ComponentComposition':{'Nitrogen':0.9514604305969551,'Oxygen':0.04853956940304498},
            'Pressure':539.56,
            'Temperature':-176.664
        }
testTask3.devices['RefFlow'].setSpecificaitons(specifications)
#---------------------------------
#          Connections
#---------------------------------
connections = [['Feed','Outlet','Column','Feed1'],
               ['RefFlow', 'Outlet','Column', 'Reflux']]
testTask3.addConnections(connections)
#---------------------------------
#          Pyomo
#---------------------------------
testTask3.generatePyomoModel("pyomoModel3.py")
import InitValueTemplate
from pyomoModel3 import test_model3
InitValueTemplate.to_csv_template(test_model3, 'InitValueTemplate3.txt')
InitValueTemplate.load_init_from_template(test_model3, 'InitValueFilled3.txt')

from pyomo.environ import *
solver=SolverFactory('ipopt')
results = solver.solve(test_model3,tee=True)
with open('reflux_display.txt', 'w') as file:
    test_model3.display(ostream=file)
