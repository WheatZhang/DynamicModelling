import sys
sys.path.append("../")
import ModularTask
#---------------------------------
#     General Setting
#---------------------------------
component = ['Nitrogen','Oxygen','Argon']
units = {'T':'℃',
         'P':'kPa',
         'F':'kmol/h',
         'h':'kJ/kmol',
         'Volumn':'m3',
         'Length':'m'}
testTask = ModularTask.PyomoStaticTask('test_model',component,units)
options = {
            'ConnectionMode': 'CombinedMode' # or: IsolatedMode
        }
testTask.setModelingOption(options)
#---------------------------------
#        System Parts
#---------------------------------
compositionThermo = ModularTask.VLEThermo.CstmTrinaryHPCCompo(testTask)
vap_enthalpy = ModularTask.EtlpThermo.CstmTrinaryHPCVapEtlp(testTask)
liq_enthalpy = ModularTask.EtlpThermo.CstmTrinaryHPCLiqEtlp(testTask)
bubble_point = ModularTask.TempPointThermo.HPCCondensorBubblePoint(testTask)
#---------------------------------
#             HPCFeed1
#---------------------------------
testTask.addDevice('TwoPhaseStream','HPCFeed1')
options = {
    'CompositionThermo' : compositionThermo,
    'VaporEnthalpy':vap_enthalpy,
    'LiquidEnthalpy': liq_enthalpy,
    'CreateCustimizedFile' : False
}
testTask.devices['HPCFeed1'].setModelingOption(options)
specifications = {
            # 'MolarFlow':1276,
            # 'ComponentComposition':{'Oxygen':0.2095,'Nitrogen':0.7812,'Argon':0.0093},
            # 'Pressure':563,
            # 'VaporFraction':0.98
            'MolarFlow':1276,
            'ComponentComposition':{'Oxygen':0.2095,'Nitrogen':0.7812,'Argon':0.0093},
            'Pressure':562.6,
            'VaporFraction':0.0841
}
testTask.devices['HPCFeed1'].setSpecificaitons(specifications)
#---------------------------------
#          Connections
#---------------------------------
connections = []
testTask.addConnections(connections)
#---------------------------------
#          Pyomo
#---------------------------------
testTask.generatePyomoModel("pyomoModel.py")

from pyomoModel import test_model
ModularTask.InitValueTools.to_template(test_model, 'FeedInitValueTemplate.txt')
ModularTask.InitValueTools.load_init_from_template(test_model, 'FeedInitValueFilled.txt')

from pyomo.environ import *
solver=SolverFactory('ipopt')
results = solver.solve(test_model,tee=True)
with open('Feed_SS_display.txt', 'w') as file:
    test_model.display(ostream=file)
ModularTask.InitValueTools.to_template(test_model, 'StaticInitValue.txt')