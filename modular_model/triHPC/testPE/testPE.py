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
testTask = ModularTask.PyomoPETask('test_model',component,units, number_of_case = 2)
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
            'MFlow':ModularTask.PE.CaseDependSpec(),
            'MFrac':{'Oxygen':0.2095,'Nitrogen':0.7812,'Argon':0.0093},
            'Pressure':564,
            'VF':0.98
}
testTask.devices['HPCFeed1'].setSpecificaitons(specifications)
#---------------------------------
#             HPCFeed2
#---------------------------------
testTask.addDevice('TwoPhaseStream','HPCFeed2')
options = {
    'CompositionThermo': compositionThermo,
    'VaporEnthalpy': vap_enthalpy,
    'LiquidEnthalpy': liq_enthalpy,
    'CreateCustimizedFile': False
}
testTask.devices['HPCFeed2'].setModelingOption(options)
specifications = {
            'MFlow':ModularTask.PE.CaseDependSpec(),
            'MFrac':{'Oxygen':0.2095,'Nitrogen':0.7812,'Argon':0.0093},
            'Pressure':562.6,
            'VF':0.0841
}
testTask.devices['HPCFeed2'].setSpecificaitons(specifications)
#---------------------------------
#          Column Body
#---------------------------------
testTask.addDevice('ColumnBody','HPC')
feed = {1:'TwoPhaseFeed',
        4:'TwoPhaseFeed'
        }
extraction = {6:'LiquidExtractions',
        22:'VaporExtractions'
}
testTask.devices['HPC'].setTrayInfo(42,feeds = feed,extractions=extraction)
options = {
    'TrayEfficiency': False,
    'TrayHeatLeakage' : True,
    'CompositionThermo' : compositionThermo,
    'VaporEnthalpy':vap_enthalpy,
    'LiquidEnthalpy': liq_enthalpy,
    'PressureProfile' : 'SimpleLinear',
    'CreateCustimizedFile' : False
}
testTask.devices['HPC'].setModelingOption(options)
specifications = {
    'TopPressure':538.6,
    'BtmPressure':564,
    'Ext6MFlow':829.8,
    'Ext22MFlow':47.29,
    "UALeakage":ModularTask.PE.EstimatedSpec({'within':'Nonnegative','init':10}),
    "AmbientTemp":ModularTask.PE.EstimatedSpec({'within':(10,40),'init':25})
}
testTask.devices['HPC'].setSpecificaitons(specifications)
weights= {
            'FlowEquWeight':1e-3,
            'EnthalpyEquWeight':1e-5,
            'PressureEquWeight':1e-2
}
testTask.devices['HPC'].setConstraintWeight(weights)
#---------------------------------
#          Column Sump
#---------------------------------
testTask.addDevice('ColumnSump','HPCSump')
options = {
    'HoldupDensity': 'Constant',
    'LiquidEnthalpy': liq_enthalpy
}
testTask.devices['HPCSump'].setModelingOption(options)
specifications = {
    'LiqRho' : 1000,
    'LevelSP' : 0.5
}
testTask.devices['HPCSump'].setSpecificaitons(specifications)
device_params = {
    'SumpCSArea' : 6,
    'ControllerKc' : -1,
    'ControllerTi' : 100
}
testTask.devices['HPCSump'].setDeviceParams(device_params)
weights= {
            'FlowEquWeight':1e-3,
}
testTask.devices['HPCSump'].setConstraintWeight(weights)
#---------------------------------
#          Condensor
#---------------------------------
testTask.addDevice('NaiveTotalCondensor','HPCCond')
options = {
    'BubblePoint': bubble_point,
    'LiquidEnthalpy': liq_enthalpy,
    'Pressure' : 'SameWithInlet',
    'CreateCustimizedFile' : False
}
testTask.devices['HPCCond'].setModelingOption(options)
specifications = {
    'RefluxRatio':0.5646495,
}
testTask.devices['HPCCond'].setSpecificaitons(specifications)
weights= {
            'FlowEquWeight':1e-3,
            'EnthalpyEquWeight':1e-5
}
testTask.devices['HPCCond'].setConstraintWeight(weights)
#---------------------------------
#          Connections
#---------------------------------
connections = [['HPCFeed1','Outlet','HPC','Feed1'],
               ['HPCFeed2','Outlet','HPC','Feed4'],
               ['HPC','ToCondensor','HPCCond','Inlet'],
               ['HPCCond', 'Reflux','HPC', 'Reflux'],
               ['HPC','SumpOutlet','HPCSump','Inlet']]
testTask.addConnections(connections)
#---------------------------------
#          Pyomo
#---------------------------------
testTask.add_case(setting='PE_Files/PE_case0.txt', init='PE_Files/init_filled0.txt')
testTask.add_case(setting='PE_Files/PE_case1.txt', init='PE_Files/init_filled1.txt')
testTask.generateCompleteModel("pyomoPE.py")
from pyomoPE import test_model
# ModularTask.PE.to_setting_template(test_model, testTask, 'PE_Files/set_template.txt')
# ModularTask.PE.to_init_template(test_model, testTask, 'PE_Files/init_template.txt')

ModularTask.PE.load_PE_init_from_templ(test_model, testTask)

from pyomo.environ import *
solver=SolverFactory('ipopt')
results = solver.solve(test_model,tee=True)
with open('PE_display.txt', 'w') as file:
    test_model.display(ostream=file)
ModularTask.InitValueTools.to_template(test_model, 'PE_result.txt')
ModularTask.PE.write_PE_report(test_model, testTask, 'PE_report.txt')