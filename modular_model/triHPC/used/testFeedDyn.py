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
testTask = ModularTask.PyomoDynamicTask('test_model',component,units)
options = {
            'ConnectionMode': 'CombinedMode' # or: IsolatedMode
        }
testTask.setModelingOption(options)
testTask.setSimulationTime((0,10), 10)
#---------------------------------
#        System Parts
#---------------------------------
compositionThermo = ModularTask.VLEThermo.CstmTrinaryHPCCompo(testTask)
hydraulics = ModularTask.Hydraulics.SimpleHydraulics(testTask)
hydraulics.setParameterValue({"k":10})
vap_enthalpy = ModularTask.EtlpThermo.CstmTrinaryHPCVapEtlp(testTask)
liq_enthalpy = ModularTask.EtlpThermo.CstmTrinaryHPCLiqEtlp(testTask)
bubble_point = ModularTask.TempPointThermo.HPCCondensorBubblePoint(testTask)
index_reduce_thermo = ModularTask.SpecialThermo.HPCIndexReduRelatedThermo(testTask)
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
            'MolarFlow':3326,
            'ComponentComposition':{'Oxygen':0.2095,'Nitrogen':0.7812,'Argon':0.0093},
            'Pressure':564,
            'VaporFraction':0.98
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
testTask.loadStaticInitValue("StaticInitValue.txt")
testTask.getNaiveDynamicInitValue()
testTask.generatePyomoModel("pyomoDyn.py")

from pyomoDyn import test_model

from pyomo.environ import *
solver=SolverFactory('ipopt')
results = solver.solve(test_model,tee=True)
with open('dynamic_display.txt', 'w') as file:
    test_model.display(ostream=file)