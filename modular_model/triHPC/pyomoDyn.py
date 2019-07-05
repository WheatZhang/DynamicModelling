from pyomo.environ import *
from pyomo.dae import *
import ModularTask

test_model = ConcreteModel()
test_model.Component = Set(initialize=['Nitrogen', 'Oxygen', 'Argon'])

#===================================
#
#      Modelling Time
#
#===================================
Discretizer = ModularTask.RuntimeTools.TimeDiscretizer(nfe=10, ncp=3, bounds=(0, 1))
Discretizer.set_fe_point(None)
Discretizer.initialize_time(test_model, 'Time')
pe_list = Discretizer.get_para_time()
test_model.ParaTime = Set(initialize=pe_list)

#===================================
#
#      Process Parts
#
#===================================
import triHPCThermo.HPCFeed1SelfCstmVapEtlp
import triHPCThermo.HPCFeed1SelfCstmLiqEtlp
import triHPCThermo.HPCFeed1SelfCstmLiqO2
import triHPCThermo.HPCFeed1SelfCstmVapO2
import triHPCThermo.HPCFeed1SelfCstmVapN2
import triHPCThermo.HPCFeed2SelfCstmVapEtlp
import triHPCThermo.HPCFeed2SelfCstmLiqEtlp
import triHPCThermo.HPCFeed2SelfCstmLiqO2
import triHPCThermo.HPCFeed2SelfCstmVapO2
import triHPCThermo.HPCFeed2SelfCstmVapN2
import triHPCThermo.HPCAllTrays1CstmVapEtlp
import triHPCThermo.HPCAllTrays2CstmVapEtlp
import triHPCThermo.HPCAllTrays3CstmVapEtlp
import triHPCThermo.HPCAllTrays4CstmVapEtlp
import triHPCThermo.HPCAllTrays5CstmVapEtlp
import triHPCThermo.HPCAllTrays6CstmVapEtlp
import triHPCThermo.HPCAllTrays7CstmVapEtlp
import triHPCThermo.HPCAllTrays8CstmVapEtlp
import triHPCThermo.HPCAllTrays9CstmVapEtlp
import triHPCThermo.HPCAllTrays10CstmVapEtlp
import triHPCThermo.HPCAllTrays11CstmVapEtlp
import triHPCThermo.HPCAllTrays12CstmVapEtlp
import triHPCThermo.HPCAllTrays13CstmVapEtlp
import triHPCThermo.HPCAllTrays14CstmVapEtlp
import triHPCThermo.HPCAllTrays15CstmVapEtlp
import triHPCThermo.HPCAllTrays16CstmVapEtlp
import triHPCThermo.HPCAllTrays17CstmVapEtlp
import triHPCThermo.HPCAllTrays18CstmVapEtlp
import triHPCThermo.HPCAllTrays19CstmVapEtlp
import triHPCThermo.HPCAllTrays20CstmVapEtlp
import triHPCThermo.HPCAllTrays21CstmVapEtlp
import triHPCThermo.HPCAllTrays22CstmVapEtlp
import triHPCThermo.HPCAllTrays23CstmVapEtlp
import triHPCThermo.HPCAllTrays24CstmVapEtlp
import triHPCThermo.HPCAllTrays25CstmVapEtlp
import triHPCThermo.HPCAllTrays26CstmVapEtlp
import triHPCThermo.HPCAllTrays27CstmVapEtlp
import triHPCThermo.HPCAllTrays28CstmVapEtlp
import triHPCThermo.HPCAllTrays29CstmVapEtlp
import triHPCThermo.HPCAllTrays30CstmVapEtlp
import triHPCThermo.HPCAllTrays31CstmVapEtlp
import triHPCThermo.HPCAllTrays32CstmVapEtlp
import triHPCThermo.HPCAllTrays33CstmVapEtlp
import triHPCThermo.HPCAllTrays34CstmVapEtlp
import triHPCThermo.HPCAllTrays35CstmVapEtlp
import triHPCThermo.HPCAllTrays36CstmVapEtlp
import triHPCThermo.HPCAllTrays37CstmVapEtlp
import triHPCThermo.HPCAllTrays38CstmVapEtlp
import triHPCThermo.HPCAllTrays39CstmVapEtlp
import triHPCThermo.HPCAllTrays40CstmVapEtlp
import triHPCThermo.HPCAllTrays41CstmVapEtlp
import triHPCThermo.HPCAllTrays42CstmVapEtlp
import triHPCThermo.HPCAllTrays1CstmLiqEtlp
import triHPCThermo.HPCAllTrays2CstmLiqEtlp
import triHPCThermo.HPCAllTrays3CstmLiqEtlp
import triHPCThermo.HPCAllTrays4CstmLiqEtlp
import triHPCThermo.HPCAllTrays5CstmLiqEtlp
import triHPCThermo.HPCAllTrays6CstmLiqEtlp
import triHPCThermo.HPCAllTrays7CstmLiqEtlp
import triHPCThermo.HPCAllTrays8CstmLiqEtlp
import triHPCThermo.HPCAllTrays9CstmLiqEtlp
import triHPCThermo.HPCAllTrays10CstmLiqEtlp
import triHPCThermo.HPCAllTrays11CstmLiqEtlp
import triHPCThermo.HPCAllTrays12CstmLiqEtlp
import triHPCThermo.HPCAllTrays13CstmLiqEtlp
import triHPCThermo.HPCAllTrays14CstmLiqEtlp
import triHPCThermo.HPCAllTrays15CstmLiqEtlp
import triHPCThermo.HPCAllTrays16CstmLiqEtlp
import triHPCThermo.HPCAllTrays17CstmLiqEtlp
import triHPCThermo.HPCAllTrays18CstmLiqEtlp
import triHPCThermo.HPCAllTrays19CstmLiqEtlp
import triHPCThermo.HPCAllTrays20CstmLiqEtlp
import triHPCThermo.HPCAllTrays21CstmLiqEtlp
import triHPCThermo.HPCAllTrays22CstmLiqEtlp
import triHPCThermo.HPCAllTrays23CstmLiqEtlp
import triHPCThermo.HPCAllTrays24CstmLiqEtlp
import triHPCThermo.HPCAllTrays25CstmLiqEtlp
import triHPCThermo.HPCAllTrays26CstmLiqEtlp
import triHPCThermo.HPCAllTrays27CstmLiqEtlp
import triHPCThermo.HPCAllTrays28CstmLiqEtlp
import triHPCThermo.HPCAllTrays29CstmLiqEtlp
import triHPCThermo.HPCAllTrays30CstmLiqEtlp
import triHPCThermo.HPCAllTrays31CstmLiqEtlp
import triHPCThermo.HPCAllTrays32CstmLiqEtlp
import triHPCThermo.HPCAllTrays33CstmLiqEtlp
import triHPCThermo.HPCAllTrays34CstmLiqEtlp
import triHPCThermo.HPCAllTrays35CstmLiqEtlp
import triHPCThermo.HPCAllTrays36CstmLiqEtlp
import triHPCThermo.HPCAllTrays37CstmLiqEtlp
import triHPCThermo.HPCAllTrays38CstmLiqEtlp
import triHPCThermo.HPCAllTrays39CstmLiqEtlp
import triHPCThermo.HPCAllTrays40CstmLiqEtlp
import triHPCThermo.HPCAllTrays41CstmLiqEtlp
import triHPCThermo.HPCAllTrays42CstmLiqEtlp
import triHPCThermo.HPCAllTrays1CstmLiqO2
import triHPCThermo.HPCAllTrays1CstmVapO2
import triHPCThermo.HPCAllTrays1CstmVapN2
import triHPCThermo.HPCAllTrays2CstmLiqO2
import triHPCThermo.HPCAllTrays2CstmVapO2
import triHPCThermo.HPCAllTrays2CstmVapN2
import triHPCThermo.HPCAllTrays3CstmLiqO2
import triHPCThermo.HPCAllTrays3CstmVapO2
import triHPCThermo.HPCAllTrays3CstmVapN2
import triHPCThermo.HPCAllTrays4CstmLiqO2
import triHPCThermo.HPCAllTrays4CstmVapO2
import triHPCThermo.HPCAllTrays4CstmVapN2
import triHPCThermo.HPCAllTrays5CstmLiqO2
import triHPCThermo.HPCAllTrays5CstmVapO2
import triHPCThermo.HPCAllTrays5CstmVapN2
import triHPCThermo.HPCAllTrays6CstmLiqO2
import triHPCThermo.HPCAllTrays6CstmVapO2
import triHPCThermo.HPCAllTrays6CstmVapN2
import triHPCThermo.HPCAllTrays7CstmLiqO2
import triHPCThermo.HPCAllTrays7CstmVapO2
import triHPCThermo.HPCAllTrays7CstmVapN2
import triHPCThermo.HPCAllTrays8CstmLiqO2
import triHPCThermo.HPCAllTrays8CstmVapO2
import triHPCThermo.HPCAllTrays8CstmVapN2
import triHPCThermo.HPCAllTrays9CstmLiqO2
import triHPCThermo.HPCAllTrays9CstmVapO2
import triHPCThermo.HPCAllTrays9CstmVapN2
import triHPCThermo.HPCAllTrays10CstmLiqO2
import triHPCThermo.HPCAllTrays10CstmVapO2
import triHPCThermo.HPCAllTrays10CstmVapN2
import triHPCThermo.HPCAllTrays11CstmLiqO2
import triHPCThermo.HPCAllTrays11CstmVapO2
import triHPCThermo.HPCAllTrays11CstmVapN2
import triHPCThermo.HPCAllTrays12CstmLiqO2
import triHPCThermo.HPCAllTrays12CstmVapO2
import triHPCThermo.HPCAllTrays12CstmVapN2
import triHPCThermo.HPCAllTrays13CstmLiqO2
import triHPCThermo.HPCAllTrays13CstmVapO2
import triHPCThermo.HPCAllTrays13CstmVapN2
import triHPCThermo.HPCAllTrays14CstmLiqO2
import triHPCThermo.HPCAllTrays14CstmVapO2
import triHPCThermo.HPCAllTrays14CstmVapN2
import triHPCThermo.HPCAllTrays15CstmLiqO2
import triHPCThermo.HPCAllTrays15CstmVapO2
import triHPCThermo.HPCAllTrays15CstmVapN2
import triHPCThermo.HPCAllTrays16CstmLiqO2
import triHPCThermo.HPCAllTrays16CstmVapO2
import triHPCThermo.HPCAllTrays16CstmVapN2
import triHPCThermo.HPCAllTrays17CstmLiqO2
import triHPCThermo.HPCAllTrays17CstmVapO2
import triHPCThermo.HPCAllTrays17CstmVapN2
import triHPCThermo.HPCAllTrays18CstmLiqO2
import triHPCThermo.HPCAllTrays18CstmVapO2
import triHPCThermo.HPCAllTrays18CstmVapN2
import triHPCThermo.HPCAllTrays19CstmLiqO2
import triHPCThermo.HPCAllTrays19CstmVapO2
import triHPCThermo.HPCAllTrays19CstmVapN2
import triHPCThermo.HPCAllTrays20CstmLiqO2
import triHPCThermo.HPCAllTrays20CstmVapO2
import triHPCThermo.HPCAllTrays20CstmVapN2
import triHPCThermo.HPCAllTrays21CstmLiqO2
import triHPCThermo.HPCAllTrays21CstmVapO2
import triHPCThermo.HPCAllTrays21CstmVapN2
import triHPCThermo.HPCAllTrays22CstmLiqO2
import triHPCThermo.HPCAllTrays22CstmVapO2
import triHPCThermo.HPCAllTrays22CstmVapN2
import triHPCThermo.HPCAllTrays23CstmLiqO2
import triHPCThermo.HPCAllTrays23CstmVapO2
import triHPCThermo.HPCAllTrays23CstmVapN2
import triHPCThermo.HPCAllTrays24CstmLiqO2
import triHPCThermo.HPCAllTrays24CstmVapO2
import triHPCThermo.HPCAllTrays24CstmVapN2
import triHPCThermo.HPCAllTrays25CstmLiqO2
import triHPCThermo.HPCAllTrays25CstmVapO2
import triHPCThermo.HPCAllTrays25CstmVapN2
import triHPCThermo.HPCAllTrays26CstmLiqO2
import triHPCThermo.HPCAllTrays26CstmVapO2
import triHPCThermo.HPCAllTrays26CstmVapN2
import triHPCThermo.HPCAllTrays27CstmLiqO2
import triHPCThermo.HPCAllTrays27CstmVapO2
import triHPCThermo.HPCAllTrays27CstmVapN2
import triHPCThermo.HPCAllTrays28CstmLiqO2
import triHPCThermo.HPCAllTrays28CstmVapO2
import triHPCThermo.HPCAllTrays28CstmVapN2
import triHPCThermo.HPCAllTrays29CstmLiqO2
import triHPCThermo.HPCAllTrays29CstmVapO2
import triHPCThermo.HPCAllTrays29CstmVapN2
import triHPCThermo.HPCAllTrays30CstmLiqO2
import triHPCThermo.HPCAllTrays30CstmVapO2
import triHPCThermo.HPCAllTrays30CstmVapN2
import triHPCThermo.HPCAllTrays31CstmLiqO2
import triHPCThermo.HPCAllTrays31CstmVapO2
import triHPCThermo.HPCAllTrays31CstmVapN2
import triHPCThermo.HPCAllTrays32CstmLiqO2
import triHPCThermo.HPCAllTrays32CstmVapO2
import triHPCThermo.HPCAllTrays32CstmVapN2
import triHPCThermo.HPCAllTrays33CstmLiqO2
import triHPCThermo.HPCAllTrays33CstmVapO2
import triHPCThermo.HPCAllTrays33CstmVapN2
import triHPCThermo.HPCAllTrays34CstmLiqO2
import triHPCThermo.HPCAllTrays34CstmVapO2
import triHPCThermo.HPCAllTrays34CstmVapN2
import triHPCThermo.HPCAllTrays35CstmLiqO2
import triHPCThermo.HPCAllTrays35CstmVapO2
import triHPCThermo.HPCAllTrays35CstmVapN2
import triHPCThermo.HPCAllTrays36CstmLiqO2
import triHPCThermo.HPCAllTrays36CstmVapO2
import triHPCThermo.HPCAllTrays36CstmVapN2
import triHPCThermo.HPCAllTrays37CstmLiqO2
import triHPCThermo.HPCAllTrays37CstmVapO2
import triHPCThermo.HPCAllTrays37CstmVapN2
import triHPCThermo.HPCAllTrays38CstmLiqO2
import triHPCThermo.HPCAllTrays38CstmVapO2
import triHPCThermo.HPCAllTrays38CstmVapN2
import triHPCThermo.HPCAllTrays39CstmLiqO2
import triHPCThermo.HPCAllTrays39CstmVapO2
import triHPCThermo.HPCAllTrays39CstmVapN2
import triHPCThermo.HPCAllTrays40CstmLiqO2
import triHPCThermo.HPCAllTrays40CstmVapO2
import triHPCThermo.HPCAllTrays40CstmVapN2
import triHPCThermo.HPCAllTrays41CstmLiqO2
import triHPCThermo.HPCAllTrays41CstmVapO2
import triHPCThermo.HPCAllTrays41CstmVapN2
import triHPCThermo.HPCAllTrays42CstmLiqO2
import triHPCThermo.HPCAllTrays42CstmVapO2
import triHPCThermo.HPCAllTrays42CstmVapN2
import triHPCThermo.HPCAllTrays1CstmLiqEtlp_pT
import triHPCThermo.HPCAllTrays1CstmLiqEtlp_pP
import triHPCThermo.HPCAllTrays1CstmLiqEtlp_px_N2
import triHPCThermo.HPCAllTrays1CstmLiqO2_pT
import triHPCThermo.HPCAllTrays1CstmLiqO2_pP
import triHPCThermo.HPCAllTrays1CstmLiqO2_px_N2
import triHPCThermo.HPCAllTrays2CstmLiqEtlp_pT
import triHPCThermo.HPCAllTrays2CstmLiqEtlp_pP
import triHPCThermo.HPCAllTrays2CstmLiqEtlp_px_N2
import triHPCThermo.HPCAllTrays2CstmLiqO2_pT
import triHPCThermo.HPCAllTrays2CstmLiqO2_pP
import triHPCThermo.HPCAllTrays2CstmLiqO2_px_N2
import triHPCThermo.HPCAllTrays3CstmLiqEtlp_pT
import triHPCThermo.HPCAllTrays3CstmLiqEtlp_pP
import triHPCThermo.HPCAllTrays3CstmLiqEtlp_px_N2
import triHPCThermo.HPCAllTrays3CstmLiqO2_pT
import triHPCThermo.HPCAllTrays3CstmLiqO2_pP
import triHPCThermo.HPCAllTrays3CstmLiqO2_px_N2
import triHPCThermo.HPCAllTrays4CstmLiqEtlp_pT
import triHPCThermo.HPCAllTrays4CstmLiqEtlp_pP
import triHPCThermo.HPCAllTrays4CstmLiqEtlp_px_N2
import triHPCThermo.HPCAllTrays4CstmLiqO2_pT
import triHPCThermo.HPCAllTrays4CstmLiqO2_pP
import triHPCThermo.HPCAllTrays4CstmLiqO2_px_N2
import triHPCThermo.HPCAllTrays5CstmLiqEtlp_pT
import triHPCThermo.HPCAllTrays5CstmLiqEtlp_pP
import triHPCThermo.HPCAllTrays5CstmLiqEtlp_px_N2
import triHPCThermo.HPCAllTrays5CstmLiqO2_pT
import triHPCThermo.HPCAllTrays5CstmLiqO2_pP
import triHPCThermo.HPCAllTrays5CstmLiqO2_px_N2
import triHPCThermo.HPCAllTrays6CstmLiqEtlp_pT
import triHPCThermo.HPCAllTrays6CstmLiqEtlp_pP
import triHPCThermo.HPCAllTrays6CstmLiqEtlp_px_N2
import triHPCThermo.HPCAllTrays6CstmLiqO2_pT
import triHPCThermo.HPCAllTrays6CstmLiqO2_pP
import triHPCThermo.HPCAllTrays6CstmLiqO2_px_N2
import triHPCThermo.HPCAllTrays7CstmLiqEtlp_pT
import triHPCThermo.HPCAllTrays7CstmLiqEtlp_pP
import triHPCThermo.HPCAllTrays7CstmLiqEtlp_px_N2
import triHPCThermo.HPCAllTrays7CstmLiqO2_pT
import triHPCThermo.HPCAllTrays7CstmLiqO2_pP
import triHPCThermo.HPCAllTrays7CstmLiqO2_px_N2
import triHPCThermo.HPCAllTrays8CstmLiqEtlp_pT
import triHPCThermo.HPCAllTrays8CstmLiqEtlp_pP
import triHPCThermo.HPCAllTrays8CstmLiqEtlp_px_N2
import triHPCThermo.HPCAllTrays8CstmLiqO2_pT
import triHPCThermo.HPCAllTrays8CstmLiqO2_pP
import triHPCThermo.HPCAllTrays8CstmLiqO2_px_N2
import triHPCThermo.HPCAllTrays9CstmLiqEtlp_pT
import triHPCThermo.HPCAllTrays9CstmLiqEtlp_pP
import triHPCThermo.HPCAllTrays9CstmLiqEtlp_px_N2
import triHPCThermo.HPCAllTrays9CstmLiqO2_pT
import triHPCThermo.HPCAllTrays9CstmLiqO2_pP
import triHPCThermo.HPCAllTrays9CstmLiqO2_px_N2
import triHPCThermo.HPCAllTrays10CstmLiqEtlp_pT
import triHPCThermo.HPCAllTrays10CstmLiqEtlp_pP
import triHPCThermo.HPCAllTrays10CstmLiqEtlp_px_N2
import triHPCThermo.HPCAllTrays10CstmLiqO2_pT
import triHPCThermo.HPCAllTrays10CstmLiqO2_pP
import triHPCThermo.HPCAllTrays10CstmLiqO2_px_N2
import triHPCThermo.HPCAllTrays11CstmLiqEtlp_pT
import triHPCThermo.HPCAllTrays11CstmLiqEtlp_pP
import triHPCThermo.HPCAllTrays11CstmLiqEtlp_px_N2
import triHPCThermo.HPCAllTrays11CstmLiqO2_pT
import triHPCThermo.HPCAllTrays11CstmLiqO2_pP
import triHPCThermo.HPCAllTrays11CstmLiqO2_px_N2
import triHPCThermo.HPCAllTrays12CstmLiqEtlp_pT
import triHPCThermo.HPCAllTrays12CstmLiqEtlp_pP
import triHPCThermo.HPCAllTrays12CstmLiqEtlp_px_N2
import triHPCThermo.HPCAllTrays12CstmLiqO2_pT
import triHPCThermo.HPCAllTrays12CstmLiqO2_pP
import triHPCThermo.HPCAllTrays12CstmLiqO2_px_N2
import triHPCThermo.HPCAllTrays13CstmLiqEtlp_pT
import triHPCThermo.HPCAllTrays13CstmLiqEtlp_pP
import triHPCThermo.HPCAllTrays13CstmLiqEtlp_px_N2
import triHPCThermo.HPCAllTrays13CstmLiqO2_pT
import triHPCThermo.HPCAllTrays13CstmLiqO2_pP
import triHPCThermo.HPCAllTrays13CstmLiqO2_px_N2
import triHPCThermo.HPCAllTrays14CstmLiqEtlp_pT
import triHPCThermo.HPCAllTrays14CstmLiqEtlp_pP
import triHPCThermo.HPCAllTrays14CstmLiqEtlp_px_N2
import triHPCThermo.HPCAllTrays14CstmLiqO2_pT
import triHPCThermo.HPCAllTrays14CstmLiqO2_pP
import triHPCThermo.HPCAllTrays14CstmLiqO2_px_N2
import triHPCThermo.HPCAllTrays15CstmLiqEtlp_pT
import triHPCThermo.HPCAllTrays15CstmLiqEtlp_pP
import triHPCThermo.HPCAllTrays15CstmLiqEtlp_px_N2
import triHPCThermo.HPCAllTrays15CstmLiqO2_pT
import triHPCThermo.HPCAllTrays15CstmLiqO2_pP
import triHPCThermo.HPCAllTrays15CstmLiqO2_px_N2
import triHPCThermo.HPCAllTrays16CstmLiqEtlp_pT
import triHPCThermo.HPCAllTrays16CstmLiqEtlp_pP
import triHPCThermo.HPCAllTrays16CstmLiqEtlp_px_N2
import triHPCThermo.HPCAllTrays16CstmLiqO2_pT
import triHPCThermo.HPCAllTrays16CstmLiqO2_pP
import triHPCThermo.HPCAllTrays16CstmLiqO2_px_N2
import triHPCThermo.HPCAllTrays17CstmLiqEtlp_pT
import triHPCThermo.HPCAllTrays17CstmLiqEtlp_pP
import triHPCThermo.HPCAllTrays17CstmLiqEtlp_px_N2
import triHPCThermo.HPCAllTrays17CstmLiqO2_pT
import triHPCThermo.HPCAllTrays17CstmLiqO2_pP
import triHPCThermo.HPCAllTrays17CstmLiqO2_px_N2
import triHPCThermo.HPCAllTrays18CstmLiqEtlp_pT
import triHPCThermo.HPCAllTrays18CstmLiqEtlp_pP
import triHPCThermo.HPCAllTrays18CstmLiqEtlp_px_N2
import triHPCThermo.HPCAllTrays18CstmLiqO2_pT
import triHPCThermo.HPCAllTrays18CstmLiqO2_pP
import triHPCThermo.HPCAllTrays18CstmLiqO2_px_N2
import triHPCThermo.HPCAllTrays19CstmLiqEtlp_pT
import triHPCThermo.HPCAllTrays19CstmLiqEtlp_pP
import triHPCThermo.HPCAllTrays19CstmLiqEtlp_px_N2
import triHPCThermo.HPCAllTrays19CstmLiqO2_pT
import triHPCThermo.HPCAllTrays19CstmLiqO2_pP
import triHPCThermo.HPCAllTrays19CstmLiqO2_px_N2
import triHPCThermo.HPCAllTrays20CstmLiqEtlp_pT
import triHPCThermo.HPCAllTrays20CstmLiqEtlp_pP
import triHPCThermo.HPCAllTrays20CstmLiqEtlp_px_N2
import triHPCThermo.HPCAllTrays20CstmLiqO2_pT
import triHPCThermo.HPCAllTrays20CstmLiqO2_pP
import triHPCThermo.HPCAllTrays20CstmLiqO2_px_N2
import triHPCThermo.HPCAllTrays21CstmLiqEtlp_pT
import triHPCThermo.HPCAllTrays21CstmLiqEtlp_pP
import triHPCThermo.HPCAllTrays21CstmLiqEtlp_px_N2
import triHPCThermo.HPCAllTrays21CstmLiqO2_pT
import triHPCThermo.HPCAllTrays21CstmLiqO2_pP
import triHPCThermo.HPCAllTrays21CstmLiqO2_px_N2
import triHPCThermo.HPCAllTrays22CstmLiqEtlp_pT
import triHPCThermo.HPCAllTrays22CstmLiqEtlp_pP
import triHPCThermo.HPCAllTrays22CstmLiqEtlp_px_N2
import triHPCThermo.HPCAllTrays22CstmLiqO2_pT
import triHPCThermo.HPCAllTrays22CstmLiqO2_pP
import triHPCThermo.HPCAllTrays22CstmLiqO2_px_N2
import triHPCThermo.HPCAllTrays23CstmLiqEtlp_pT
import triHPCThermo.HPCAllTrays23CstmLiqEtlp_pP
import triHPCThermo.HPCAllTrays23CstmLiqEtlp_px_N2
import triHPCThermo.HPCAllTrays23CstmLiqO2_pT
import triHPCThermo.HPCAllTrays23CstmLiqO2_pP
import triHPCThermo.HPCAllTrays23CstmLiqO2_px_N2
import triHPCThermo.HPCAllTrays24CstmLiqEtlp_pT
import triHPCThermo.HPCAllTrays24CstmLiqEtlp_pP
import triHPCThermo.HPCAllTrays24CstmLiqEtlp_px_N2
import triHPCThermo.HPCAllTrays24CstmLiqO2_pT
import triHPCThermo.HPCAllTrays24CstmLiqO2_pP
import triHPCThermo.HPCAllTrays24CstmLiqO2_px_N2
import triHPCThermo.HPCAllTrays25CstmLiqEtlp_pT
import triHPCThermo.HPCAllTrays25CstmLiqEtlp_pP
import triHPCThermo.HPCAllTrays25CstmLiqEtlp_px_N2
import triHPCThermo.HPCAllTrays25CstmLiqO2_pT
import triHPCThermo.HPCAllTrays25CstmLiqO2_pP
import triHPCThermo.HPCAllTrays25CstmLiqO2_px_N2
import triHPCThermo.HPCAllTrays26CstmLiqEtlp_pT
import triHPCThermo.HPCAllTrays26CstmLiqEtlp_pP
import triHPCThermo.HPCAllTrays26CstmLiqEtlp_px_N2
import triHPCThermo.HPCAllTrays26CstmLiqO2_pT
import triHPCThermo.HPCAllTrays26CstmLiqO2_pP
import triHPCThermo.HPCAllTrays26CstmLiqO2_px_N2
import triHPCThermo.HPCAllTrays27CstmLiqEtlp_pT
import triHPCThermo.HPCAllTrays27CstmLiqEtlp_pP
import triHPCThermo.HPCAllTrays27CstmLiqEtlp_px_N2
import triHPCThermo.HPCAllTrays27CstmLiqO2_pT
import triHPCThermo.HPCAllTrays27CstmLiqO2_pP
import triHPCThermo.HPCAllTrays27CstmLiqO2_px_N2
import triHPCThermo.HPCAllTrays28CstmLiqEtlp_pT
import triHPCThermo.HPCAllTrays28CstmLiqEtlp_pP
import triHPCThermo.HPCAllTrays28CstmLiqEtlp_px_N2
import triHPCThermo.HPCAllTrays28CstmLiqO2_pT
import triHPCThermo.HPCAllTrays28CstmLiqO2_pP
import triHPCThermo.HPCAllTrays28CstmLiqO2_px_N2
import triHPCThermo.HPCAllTrays29CstmLiqEtlp_pT
import triHPCThermo.HPCAllTrays29CstmLiqEtlp_pP
import triHPCThermo.HPCAllTrays29CstmLiqEtlp_px_N2
import triHPCThermo.HPCAllTrays29CstmLiqO2_pT
import triHPCThermo.HPCAllTrays29CstmLiqO2_pP
import triHPCThermo.HPCAllTrays29CstmLiqO2_px_N2
import triHPCThermo.HPCAllTrays30CstmLiqEtlp_pT
import triHPCThermo.HPCAllTrays30CstmLiqEtlp_pP
import triHPCThermo.HPCAllTrays30CstmLiqEtlp_px_N2
import triHPCThermo.HPCAllTrays30CstmLiqO2_pT
import triHPCThermo.HPCAllTrays30CstmLiqO2_pP
import triHPCThermo.HPCAllTrays30CstmLiqO2_px_N2
import triHPCThermo.HPCAllTrays31CstmLiqEtlp_pT
import triHPCThermo.HPCAllTrays31CstmLiqEtlp_pP
import triHPCThermo.HPCAllTrays31CstmLiqEtlp_px_N2
import triHPCThermo.HPCAllTrays31CstmLiqO2_pT
import triHPCThermo.HPCAllTrays31CstmLiqO2_pP
import triHPCThermo.HPCAllTrays31CstmLiqO2_px_N2
import triHPCThermo.HPCAllTrays32CstmLiqEtlp_pT
import triHPCThermo.HPCAllTrays32CstmLiqEtlp_pP
import triHPCThermo.HPCAllTrays32CstmLiqEtlp_px_N2
import triHPCThermo.HPCAllTrays32CstmLiqO2_pT
import triHPCThermo.HPCAllTrays32CstmLiqO2_pP
import triHPCThermo.HPCAllTrays32CstmLiqO2_px_N2
import triHPCThermo.HPCAllTrays33CstmLiqEtlp_pT
import triHPCThermo.HPCAllTrays33CstmLiqEtlp_pP
import triHPCThermo.HPCAllTrays33CstmLiqEtlp_px_N2
import triHPCThermo.HPCAllTrays33CstmLiqO2_pT
import triHPCThermo.HPCAllTrays33CstmLiqO2_pP
import triHPCThermo.HPCAllTrays33CstmLiqO2_px_N2
import triHPCThermo.HPCAllTrays34CstmLiqEtlp_pT
import triHPCThermo.HPCAllTrays34CstmLiqEtlp_pP
import triHPCThermo.HPCAllTrays34CstmLiqEtlp_px_N2
import triHPCThermo.HPCAllTrays34CstmLiqO2_pT
import triHPCThermo.HPCAllTrays34CstmLiqO2_pP
import triHPCThermo.HPCAllTrays34CstmLiqO2_px_N2
import triHPCThermo.HPCAllTrays35CstmLiqEtlp_pT
import triHPCThermo.HPCAllTrays35CstmLiqEtlp_pP
import triHPCThermo.HPCAllTrays35CstmLiqEtlp_px_N2
import triHPCThermo.HPCAllTrays35CstmLiqO2_pT
import triHPCThermo.HPCAllTrays35CstmLiqO2_pP
import triHPCThermo.HPCAllTrays35CstmLiqO2_px_N2
import triHPCThermo.HPCAllTrays36CstmLiqEtlp_pT
import triHPCThermo.HPCAllTrays36CstmLiqEtlp_pP
import triHPCThermo.HPCAllTrays36CstmLiqEtlp_px_N2
import triHPCThermo.HPCAllTrays36CstmLiqO2_pT
import triHPCThermo.HPCAllTrays36CstmLiqO2_pP
import triHPCThermo.HPCAllTrays36CstmLiqO2_px_N2
import triHPCThermo.HPCAllTrays37CstmLiqEtlp_pT
import triHPCThermo.HPCAllTrays37CstmLiqEtlp_pP
import triHPCThermo.HPCAllTrays37CstmLiqEtlp_px_N2
import triHPCThermo.HPCAllTrays37CstmLiqO2_pT
import triHPCThermo.HPCAllTrays37CstmLiqO2_pP
import triHPCThermo.HPCAllTrays37CstmLiqO2_px_N2
import triHPCThermo.HPCAllTrays38CstmLiqEtlp_pT
import triHPCThermo.HPCAllTrays38CstmLiqEtlp_pP
import triHPCThermo.HPCAllTrays38CstmLiqEtlp_px_N2
import triHPCThermo.HPCAllTrays38CstmLiqO2_pT
import triHPCThermo.HPCAllTrays38CstmLiqO2_pP
import triHPCThermo.HPCAllTrays38CstmLiqO2_px_N2
import triHPCThermo.HPCAllTrays39CstmLiqEtlp_pT
import triHPCThermo.HPCAllTrays39CstmLiqEtlp_pP
import triHPCThermo.HPCAllTrays39CstmLiqEtlp_px_N2
import triHPCThermo.HPCAllTrays39CstmLiqO2_pT
import triHPCThermo.HPCAllTrays39CstmLiqO2_pP
import triHPCThermo.HPCAllTrays39CstmLiqO2_px_N2
import triHPCThermo.HPCAllTrays40CstmLiqEtlp_pT
import triHPCThermo.HPCAllTrays40CstmLiqEtlp_pP
import triHPCThermo.HPCAllTrays40CstmLiqEtlp_px_N2
import triHPCThermo.HPCAllTrays40CstmLiqO2_pT
import triHPCThermo.HPCAllTrays40CstmLiqO2_pP
import triHPCThermo.HPCAllTrays40CstmLiqO2_px_N2
import triHPCThermo.HPCAllTrays41CstmLiqEtlp_pT
import triHPCThermo.HPCAllTrays41CstmLiqEtlp_pP
import triHPCThermo.HPCAllTrays41CstmLiqEtlp_px_N2
import triHPCThermo.HPCAllTrays41CstmLiqO2_pT
import triHPCThermo.HPCAllTrays41CstmLiqO2_pP
import triHPCThermo.HPCAllTrays41CstmLiqO2_px_N2
import triHPCThermo.HPCAllTrays42CstmLiqEtlp_pT
import triHPCThermo.HPCAllTrays42CstmLiqEtlp_pP
import triHPCThermo.HPCAllTrays42CstmLiqEtlp_px_N2
import triHPCThermo.HPCAllTrays42CstmLiqO2_pT
import triHPCThermo.HPCAllTrays42CstmLiqO2_pP
import triHPCThermo.HPCAllTrays42CstmLiqO2_px_N2
import triHPCThermo.HPCSumpHdlpCstmLiqEtlp
import triHPCThermo.HPCCondOutletCstmLiqEtlp
import triHPCThermo.HPCCondSelfCstmLiqO2

#===================================
#
#      Parameters & Sets
#
#===================================
#--------HPCFeed1---------
old_time = [0, 0.1, 0.11]
old_dict = {0: 3326, 0.1: 3326, 0.11: 3492.3}
new_dict = ModularTask.RuntimeTools.modify_time(old_dict, pe_list, old_time)
test_model.HPCFeed1MFlow = Param(test_model.ParaTime, initialize = new_dict)
old_dict = {}
for i in test_model.ParaTime.value:
	old_dict[i,"Oxygen"] = 0.2095
	old_dict[i,"Nitrogen"] = 0.7812
	old_dict[i,"Argon"] = 0.0093
test_model.HPCFeed1MFrac = Param(test_model.ParaTime, test_model.Component, initialize = old_dict)
test_model.HPCFeed1Pressure = Param(test_model.ParaTime, initialize = 564.000000)
test_model.HPCFeed1VF = Param(test_model.ParaTime, initialize = 0.980000)
#--------HPCFeed2---------
test_model.HPCFeed2MFlow = Param(test_model.ParaTime, initialize = 1276.000000)
old_dict = {}
for i in test_model.ParaTime.value:
	old_dict[i,"Oxygen"] = 0.2095
	old_dict[i,"Nitrogen"] = 0.7812
	old_dict[i,"Argon"] = 0.0093
test_model.HPCFeed2MFrac = Param(test_model.ParaTime, test_model.Component, initialize = old_dict)
test_model.HPCFeed2Pressure = Param(test_model.ParaTime, initialize = 562.600000)
test_model.HPCFeed2VF = Param(test_model.ParaTime, initialize = 0.084100)
#--------HPC---------
test_model.HPCTrays = RangeSet(1, 42)
test_model.HPCExt6MFlow = Param(test_model.ParaTime, initialize = 829.800000)
test_model.HPCExt22MFlow = Param(test_model.ParaTime, initialize = 47.290000)
old_time = [0, 0.1, 0.11]
old_dict = {0: 538.6, 0.1: 538.6, 0.11: 549.3720000000001}
new_dict = ModularTask.RuntimeTools.modify_time(old_dict, pe_list, old_time)
test_model.HPCTopPressure = Param(test_model.ParaTime, initialize = new_dict)
test_model.HPCBtmPressure = Param(test_model.ParaTime, initialize = 564.000000)
test_model.HPCAllTraysHydroParak = Param(initialize=10.000000)
test_model.HPCUALeakage = Param(test_model.ParaTime, initialize = 0.000000)
test_model.HPCAmbientTemp = Param(test_model.ParaTime, initialize = 25.000000)
#--------HPCSump---------
test_model.HPCSumpLCParaKc = Param(initialize=-1.000000)
test_model.HPCSumpLCParaTi = Param(initialize=100.000000)
test_model.HPCSumpLCParaMVSS = Param(initialize=2129.969185)
test_model.HPCSumpLCParaCVSS = Param(initialize=0.500000)
test_model.HPCSumpLevelSP = Param(test_model.ParaTime, initialize = 0.500000)
test_model.HPCSumpLiqRho = Param(test_model.ParaTime, initialize = 1000.000000)
test_model.HPCSumpSumpCSArea = Param(initialize = 6.000000)
#--------HPCCond---------
test_model.HPCCondRefluxRatio = Param(test_model.ParaTime, initialize = 0.564650)

#===================================
#
#         Variables
#
#===================================
#--------HPCFeed1---------
test_model.HPCFeed1Temp = Var(test_model.Time)
test_model.HPCFeed1LiqMFrac = Var(test_model.Time,test_model.Component, bounds=(0, 1))
test_model.HPCFeed1VapMFrac = Var(test_model.Time,test_model.Component, bounds=(0, 1))
#--------HPCFeed2---------
test_model.HPCFeed2Temp = Var(test_model.Time)
test_model.HPCFeed2LiqMFrac = Var(test_model.Time,test_model.Component, bounds=(0, 1))
test_model.HPCFeed2VapMFrac = Var(test_model.Time,test_model.Component, bounds=(0, 1))
#--------HPC---------
test_model.HPCVapLvMFlow = Var(test_model.Time, test_model.HPCTrays, within=NonNegativeReals)
test_model.HPCLiqLvMFlow = Var(test_model.Time, test_model.HPCTrays, within=NonNegativeReals)
test_model.HPCTrayTemp = Var(test_model.Time, test_model.HPCTrays)
test_model.HPCTrayPressure = Var(test_model.Time, test_model.HPCTrays)
test_model.HPCLiqLvMFrac = Var(test_model.Time,test_model.HPCTrays,test_model.Component, bounds=(0, 1))
test_model.HPCVapLvMFrac = Var(test_model.Time,test_model.HPCTrays,test_model.Component, bounds=(0, 1))
#--------HPC's var in extractions---------
test_model.HPCExt6MFrac = Var(test_model.Time, test_model.Component, bounds=(0,1))
test_model.HPCExt6MEtlp = Var(test_model.Time)
test_model.HPCExt22MFrac = Var(test_model.Time, test_model.Component, bounds=(0,1))
test_model.HPCExt22MEtlp = Var(test_model.Time)
#--------HPC's var in differential equations---------
test_model.HPCTrayMHldp = Var(test_model.Time, test_model.HPCTrays, within=NonNegativeReals)
test_model.HPCDtTrayMHldp = DerivativeVar(test_model.HPCTrayMHldp)
test_model.HPCTrayMCompHldp = Var(test_model.Time, test_model.HPCTrays, test_model.Component, within=NonNegativeReals)
test_model.HPCDtTrayMCompHldp = DerivativeVar(test_model.HPCTrayMCompHldp)
test_model.HPCDtTrayMEtlpHldp = Var(test_model.Time, test_model.HPCTrays)
test_model.HPCDtTrayPressure = DerivativeVar(test_model.HPCTrayPressure)
#--------HPCSump---------
test_model.HPCSumpLCSumError = Var(test_model.Time, initialize=0)
test_model.HPCSumpLCError = DerivativeVar(test_model.HPCSumpLCSumError,initialize=0)
test_model.HPCSumpOutMFlow = Var(test_model.Time, within=NonNegativeReals)
test_model.HPCSumpMCompHldp = Var(test_model.Time, test_model.Component, within=NonNegativeReals)
test_model.HPCSumpDtMCompHldp = DerivativeVar(test_model.HPCSumpMCompHldp)
test_model.HPCSumpHldpLevel = Var(test_model.Time, within=NonNegativeReals)
test_model.HPCSumpMHldp = Var(test_model.Time, within=NonNegativeReals)
test_model.HPCSumpHldpMFrac = Var(test_model.Time, test_model.Component, bounds =(0,1))
#--------HPCCond---------
test_model.HPCCondRefMFlow = Var(test_model.Time, within=NonNegativeReals)
test_model.HPCCondPrdtMFlow = Var(test_model.Time, within=NonNegativeReals)
test_model.HPCCondMHeatOut = Var(test_model.Time, within=NonNegativeReals)
test_model.HPCCondTemp = Var(test_model.Time,initialize = 0)

#===================================
#
#         Expressions
#
#===================================
#--------HPCFeed1 Enthalpy---------
def HPCFeed1VapMEtlp(m,time):
	return triHPCThermo.HPCFeed1SelfCstmVapEtlp.VapEtlp(m.HPCFeed1Pressure[time], m.HPCFeed1Temp[time],m.HPCFeed1LiqMFrac[time,"Nitrogen"])
test_model.HPCFeed1VapMEtlp = Expression(test_model.Time,rule=HPCFeed1VapMEtlp)
def HPCFeed1LiqMEtlp(m,time):
	return triHPCThermo.HPCFeed1SelfCstmLiqEtlp.LiqEtlp(m.HPCFeed1Pressure[time], m.HPCFeed1Temp[time],m.HPCFeed1LiqMFrac[time,"Nitrogen"])
test_model.HPCFeed1LiqMEtlp = Expression(test_model.Time,rule=HPCFeed1LiqMEtlp)
def HPCFeed1MEtlp(m, time):
	return m.HPCFeed1LiqMEtlp[time] * (1-m.HPCFeed1VF[time])+m.HPCFeed1VapMEtlp[time] * m.HPCFeed1VF[time]
test_model.HPCFeed1MEtlp = Expression(test_model.Time, rule=HPCFeed1MEtlp)
#--------HPCFeed2 Enthalpy---------
def HPCFeed2VapMEtlp(m,time):
	return triHPCThermo.HPCFeed2SelfCstmVapEtlp.VapEtlp(m.HPCFeed2Pressure[time], m.HPCFeed2Temp[time],m.HPCFeed2LiqMFrac[time,"Nitrogen"])
test_model.HPCFeed2VapMEtlp = Expression(test_model.Time,rule=HPCFeed2VapMEtlp)
def HPCFeed2LiqMEtlp(m,time):
	return triHPCThermo.HPCFeed2SelfCstmLiqEtlp.LiqEtlp(m.HPCFeed2Pressure[time], m.HPCFeed2Temp[time],m.HPCFeed2LiqMFrac[time,"Nitrogen"])
test_model.HPCFeed2LiqMEtlp = Expression(test_model.Time,rule=HPCFeed2LiqMEtlp)
def HPCFeed2MEtlp(m, time):
	return m.HPCFeed2LiqMEtlp[time] * (1-m.HPCFeed2VF[time])+m.HPCFeed2VapMEtlp[time] * m.HPCFeed2VF[time]
test_model.HPCFeed2MEtlp = Expression(test_model.Time, rule=HPCFeed2MEtlp)
#--------HPC Component Flowrate---------
def HPCVapLvMCompFlow(m, time, tray, comp):
	return m.HPCVapLvMFrac[time, tray, comp] * m.HPCVapLvMFlow[time, tray]
test_model.HPCVapLvMCompFlow = Expression(test_model.Time, test_model.HPCTrays, test_model.Component, rule=HPCVapLvMCompFlow)
def HPCLiqLvMCompFlow(m, time, tray, comp):
	return m.HPCLiqLvMFrac[time, tray, comp] * m.HPCLiqLvMFlow[time, tray]
test_model.HPCLiqLvMCompFlow = Expression(test_model.Time, test_model.HPCTrays, test_model.Component, rule=HPCLiqLvMCompFlow)
#--------HPC Thermo and Enthalpy---------
def HPCVapLvMEtlp(m,time,tray):
	if tray==1:
		return triHPCThermo.HPCAllTrays1CstmVapEtlp.VapEtlp(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==2:
		return triHPCThermo.HPCAllTrays2CstmVapEtlp.VapEtlp(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==3:
		return triHPCThermo.HPCAllTrays3CstmVapEtlp.VapEtlp(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==4:
		return triHPCThermo.HPCAllTrays4CstmVapEtlp.VapEtlp(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==5:
		return triHPCThermo.HPCAllTrays5CstmVapEtlp.VapEtlp(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==6:
		return triHPCThermo.HPCAllTrays6CstmVapEtlp.VapEtlp(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==7:
		return triHPCThermo.HPCAllTrays7CstmVapEtlp.VapEtlp(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==8:
		return triHPCThermo.HPCAllTrays8CstmVapEtlp.VapEtlp(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==9:
		return triHPCThermo.HPCAllTrays9CstmVapEtlp.VapEtlp(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==10:
		return triHPCThermo.HPCAllTrays10CstmVapEtlp.VapEtlp(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==11:
		return triHPCThermo.HPCAllTrays11CstmVapEtlp.VapEtlp(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==12:
		return triHPCThermo.HPCAllTrays12CstmVapEtlp.VapEtlp(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==13:
		return triHPCThermo.HPCAllTrays13CstmVapEtlp.VapEtlp(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==14:
		return triHPCThermo.HPCAllTrays14CstmVapEtlp.VapEtlp(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==15:
		return triHPCThermo.HPCAllTrays15CstmVapEtlp.VapEtlp(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==16:
		return triHPCThermo.HPCAllTrays16CstmVapEtlp.VapEtlp(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==17:
		return triHPCThermo.HPCAllTrays17CstmVapEtlp.VapEtlp(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==18:
		return triHPCThermo.HPCAllTrays18CstmVapEtlp.VapEtlp(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==19:
		return triHPCThermo.HPCAllTrays19CstmVapEtlp.VapEtlp(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==20:
		return triHPCThermo.HPCAllTrays20CstmVapEtlp.VapEtlp(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==21:
		return triHPCThermo.HPCAllTrays21CstmVapEtlp.VapEtlp(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==22:
		return triHPCThermo.HPCAllTrays22CstmVapEtlp.VapEtlp(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==23:
		return triHPCThermo.HPCAllTrays23CstmVapEtlp.VapEtlp(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==24:
		return triHPCThermo.HPCAllTrays24CstmVapEtlp.VapEtlp(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==25:
		return triHPCThermo.HPCAllTrays25CstmVapEtlp.VapEtlp(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==26:
		return triHPCThermo.HPCAllTrays26CstmVapEtlp.VapEtlp(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==27:
		return triHPCThermo.HPCAllTrays27CstmVapEtlp.VapEtlp(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==28:
		return triHPCThermo.HPCAllTrays28CstmVapEtlp.VapEtlp(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==29:
		return triHPCThermo.HPCAllTrays29CstmVapEtlp.VapEtlp(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==30:
		return triHPCThermo.HPCAllTrays30CstmVapEtlp.VapEtlp(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==31:
		return triHPCThermo.HPCAllTrays31CstmVapEtlp.VapEtlp(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==32:
		return triHPCThermo.HPCAllTrays32CstmVapEtlp.VapEtlp(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==33:
		return triHPCThermo.HPCAllTrays33CstmVapEtlp.VapEtlp(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==34:
		return triHPCThermo.HPCAllTrays34CstmVapEtlp.VapEtlp(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==35:
		return triHPCThermo.HPCAllTrays35CstmVapEtlp.VapEtlp(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==36:
		return triHPCThermo.HPCAllTrays36CstmVapEtlp.VapEtlp(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==37:
		return triHPCThermo.HPCAllTrays37CstmVapEtlp.VapEtlp(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==38:
		return triHPCThermo.HPCAllTrays38CstmVapEtlp.VapEtlp(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==39:
		return triHPCThermo.HPCAllTrays39CstmVapEtlp.VapEtlp(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==40:
		return triHPCThermo.HPCAllTrays40CstmVapEtlp.VapEtlp(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==41:
		return triHPCThermo.HPCAllTrays41CstmVapEtlp.VapEtlp(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==42:
		return triHPCThermo.HPCAllTrays42CstmVapEtlp.VapEtlp(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
test_model.HPCVapLvMEtlp = Expression(test_model.Time,test_model.HPCTrays,rule=HPCVapLvMEtlp)
def HPCLiqLvMEtlp(m,time,tray):
	if tray==1:
		return triHPCThermo.HPCAllTrays1CstmLiqEtlp.LiqEtlp(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==2:
		return triHPCThermo.HPCAllTrays2CstmLiqEtlp.LiqEtlp(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==3:
		return triHPCThermo.HPCAllTrays3CstmLiqEtlp.LiqEtlp(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==4:
		return triHPCThermo.HPCAllTrays4CstmLiqEtlp.LiqEtlp(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==5:
		return triHPCThermo.HPCAllTrays5CstmLiqEtlp.LiqEtlp(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==6:
		return triHPCThermo.HPCAllTrays6CstmLiqEtlp.LiqEtlp(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==7:
		return triHPCThermo.HPCAllTrays7CstmLiqEtlp.LiqEtlp(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==8:
		return triHPCThermo.HPCAllTrays8CstmLiqEtlp.LiqEtlp(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==9:
		return triHPCThermo.HPCAllTrays9CstmLiqEtlp.LiqEtlp(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==10:
		return triHPCThermo.HPCAllTrays10CstmLiqEtlp.LiqEtlp(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==11:
		return triHPCThermo.HPCAllTrays11CstmLiqEtlp.LiqEtlp(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==12:
		return triHPCThermo.HPCAllTrays12CstmLiqEtlp.LiqEtlp(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==13:
		return triHPCThermo.HPCAllTrays13CstmLiqEtlp.LiqEtlp(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==14:
		return triHPCThermo.HPCAllTrays14CstmLiqEtlp.LiqEtlp(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==15:
		return triHPCThermo.HPCAllTrays15CstmLiqEtlp.LiqEtlp(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==16:
		return triHPCThermo.HPCAllTrays16CstmLiqEtlp.LiqEtlp(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==17:
		return triHPCThermo.HPCAllTrays17CstmLiqEtlp.LiqEtlp(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==18:
		return triHPCThermo.HPCAllTrays18CstmLiqEtlp.LiqEtlp(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==19:
		return triHPCThermo.HPCAllTrays19CstmLiqEtlp.LiqEtlp(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==20:
		return triHPCThermo.HPCAllTrays20CstmLiqEtlp.LiqEtlp(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==21:
		return triHPCThermo.HPCAllTrays21CstmLiqEtlp.LiqEtlp(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==22:
		return triHPCThermo.HPCAllTrays22CstmLiqEtlp.LiqEtlp(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==23:
		return triHPCThermo.HPCAllTrays23CstmLiqEtlp.LiqEtlp(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==24:
		return triHPCThermo.HPCAllTrays24CstmLiqEtlp.LiqEtlp(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==25:
		return triHPCThermo.HPCAllTrays25CstmLiqEtlp.LiqEtlp(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==26:
		return triHPCThermo.HPCAllTrays26CstmLiqEtlp.LiqEtlp(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==27:
		return triHPCThermo.HPCAllTrays27CstmLiqEtlp.LiqEtlp(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==28:
		return triHPCThermo.HPCAllTrays28CstmLiqEtlp.LiqEtlp(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==29:
		return triHPCThermo.HPCAllTrays29CstmLiqEtlp.LiqEtlp(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==30:
		return triHPCThermo.HPCAllTrays30CstmLiqEtlp.LiqEtlp(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==31:
		return triHPCThermo.HPCAllTrays31CstmLiqEtlp.LiqEtlp(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==32:
		return triHPCThermo.HPCAllTrays32CstmLiqEtlp.LiqEtlp(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==33:
		return triHPCThermo.HPCAllTrays33CstmLiqEtlp.LiqEtlp(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==34:
		return triHPCThermo.HPCAllTrays34CstmLiqEtlp.LiqEtlp(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==35:
		return triHPCThermo.HPCAllTrays35CstmLiqEtlp.LiqEtlp(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==36:
		return triHPCThermo.HPCAllTrays36CstmLiqEtlp.LiqEtlp(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==37:
		return triHPCThermo.HPCAllTrays37CstmLiqEtlp.LiqEtlp(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==38:
		return triHPCThermo.HPCAllTrays38CstmLiqEtlp.LiqEtlp(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==39:
		return triHPCThermo.HPCAllTrays39CstmLiqEtlp.LiqEtlp(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==40:
		return triHPCThermo.HPCAllTrays40CstmLiqEtlp.LiqEtlp(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==41:
		return triHPCThermo.HPCAllTrays41CstmLiqEtlp.LiqEtlp(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==42:
		return triHPCThermo.HPCAllTrays42CstmLiqEtlp.LiqEtlp(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
test_model.HPCLiqLvMEtlp = Expression(test_model.Time,test_model.HPCTrays,rule=HPCLiqLvMEtlp)
#--------HPC Dynamic Related---------
def HPCDtLiqLvMFrac(m, time, tray, comp):
	return (m.HPCDtTrayMCompHldp[time, tray, comp] - m.HPCLiqLvMFrac[time, tray, comp] *\
	      m.HPCDtTrayMHldp[time, tray]) / m.HPCTrayMHldp[time, tray]
test_model.HPCDtLiqLvMFrac = Expression(test_model.Time, test_model.HPCTrays, test_model.Component, rule=HPCDtLiqLvMFrac)
def HPCPTTrayMEtlpHldp(m,time,tray):
	if tray==1:
		return triHPCThermo.HPCAllTrays1CstmLiqEtlp_pT.LiqEtlp_pT(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
	elif tray==2:
		return triHPCThermo.HPCAllTrays2CstmLiqEtlp_pT.LiqEtlp_pT(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
	elif tray==3:
		return triHPCThermo.HPCAllTrays3CstmLiqEtlp_pT.LiqEtlp_pT(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
	elif tray==4:
		return triHPCThermo.HPCAllTrays4CstmLiqEtlp_pT.LiqEtlp_pT(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
	elif tray==5:
		return triHPCThermo.HPCAllTrays5CstmLiqEtlp_pT.LiqEtlp_pT(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
	elif tray==6:
		return triHPCThermo.HPCAllTrays6CstmLiqEtlp_pT.LiqEtlp_pT(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
	elif tray==7:
		return triHPCThermo.HPCAllTrays7CstmLiqEtlp_pT.LiqEtlp_pT(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
	elif tray==8:
		return triHPCThermo.HPCAllTrays8CstmLiqEtlp_pT.LiqEtlp_pT(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
	elif tray==9:
		return triHPCThermo.HPCAllTrays9CstmLiqEtlp_pT.LiqEtlp_pT(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
	elif tray==10:
		return triHPCThermo.HPCAllTrays10CstmLiqEtlp_pT.LiqEtlp_pT(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
	elif tray==11:
		return triHPCThermo.HPCAllTrays11CstmLiqEtlp_pT.LiqEtlp_pT(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
	elif tray==12:
		return triHPCThermo.HPCAllTrays12CstmLiqEtlp_pT.LiqEtlp_pT(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
	elif tray==13:
		return triHPCThermo.HPCAllTrays13CstmLiqEtlp_pT.LiqEtlp_pT(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
	elif tray==14:
		return triHPCThermo.HPCAllTrays14CstmLiqEtlp_pT.LiqEtlp_pT(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
	elif tray==15:
		return triHPCThermo.HPCAllTrays15CstmLiqEtlp_pT.LiqEtlp_pT(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
	elif tray==16:
		return triHPCThermo.HPCAllTrays16CstmLiqEtlp_pT.LiqEtlp_pT(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
	elif tray==17:
		return triHPCThermo.HPCAllTrays17CstmLiqEtlp_pT.LiqEtlp_pT(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
	elif tray==18:
		return triHPCThermo.HPCAllTrays18CstmLiqEtlp_pT.LiqEtlp_pT(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
	elif tray==19:
		return triHPCThermo.HPCAllTrays19CstmLiqEtlp_pT.LiqEtlp_pT(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
	elif tray==20:
		return triHPCThermo.HPCAllTrays20CstmLiqEtlp_pT.LiqEtlp_pT(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
	elif tray==21:
		return triHPCThermo.HPCAllTrays21CstmLiqEtlp_pT.LiqEtlp_pT(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
	elif tray==22:
		return triHPCThermo.HPCAllTrays22CstmLiqEtlp_pT.LiqEtlp_pT(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
	elif tray==23:
		return triHPCThermo.HPCAllTrays23CstmLiqEtlp_pT.LiqEtlp_pT(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
	elif tray==24:
		return triHPCThermo.HPCAllTrays24CstmLiqEtlp_pT.LiqEtlp_pT(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
	elif tray==25:
		return triHPCThermo.HPCAllTrays25CstmLiqEtlp_pT.LiqEtlp_pT(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
	elif tray==26:
		return triHPCThermo.HPCAllTrays26CstmLiqEtlp_pT.LiqEtlp_pT(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
	elif tray==27:
		return triHPCThermo.HPCAllTrays27CstmLiqEtlp_pT.LiqEtlp_pT(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
	elif tray==28:
		return triHPCThermo.HPCAllTrays28CstmLiqEtlp_pT.LiqEtlp_pT(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
	elif tray==29:
		return triHPCThermo.HPCAllTrays29CstmLiqEtlp_pT.LiqEtlp_pT(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
	elif tray==30:
		return triHPCThermo.HPCAllTrays30CstmLiqEtlp_pT.LiqEtlp_pT(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
	elif tray==31:
		return triHPCThermo.HPCAllTrays31CstmLiqEtlp_pT.LiqEtlp_pT(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
	elif tray==32:
		return triHPCThermo.HPCAllTrays32CstmLiqEtlp_pT.LiqEtlp_pT(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
	elif tray==33:
		return triHPCThermo.HPCAllTrays33CstmLiqEtlp_pT.LiqEtlp_pT(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
	elif tray==34:
		return triHPCThermo.HPCAllTrays34CstmLiqEtlp_pT.LiqEtlp_pT(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
	elif tray==35:
		return triHPCThermo.HPCAllTrays35CstmLiqEtlp_pT.LiqEtlp_pT(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
	elif tray==36:
		return triHPCThermo.HPCAllTrays36CstmLiqEtlp_pT.LiqEtlp_pT(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
	elif tray==37:
		return triHPCThermo.HPCAllTrays37CstmLiqEtlp_pT.LiqEtlp_pT(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
	elif tray==38:
		return triHPCThermo.HPCAllTrays38CstmLiqEtlp_pT.LiqEtlp_pT(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
	elif tray==39:
		return triHPCThermo.HPCAllTrays39CstmLiqEtlp_pT.LiqEtlp_pT(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
	elif tray==40:
		return triHPCThermo.HPCAllTrays40CstmLiqEtlp_pT.LiqEtlp_pT(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
	elif tray==41:
		return triHPCThermo.HPCAllTrays41CstmLiqEtlp_pT.LiqEtlp_pT(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
	elif tray==42:
		return triHPCThermo.HPCAllTrays42CstmLiqEtlp_pT.LiqEtlp_pT(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
test_model.HPCPTTrayMEtlpHldp = Expression(test_model.Time,test_model.HPCTrays,rule=HPCPTTrayMEtlpHldp)
def HPCPPTrayMEtlpHldp(m,time,tray):
	if tray==1:
		return triHPCThermo.HPCAllTrays1CstmLiqEtlp_pP.LiqEtlp_pP(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
	elif tray==2:
		return triHPCThermo.HPCAllTrays2CstmLiqEtlp_pP.LiqEtlp_pP(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
	elif tray==3:
		return triHPCThermo.HPCAllTrays3CstmLiqEtlp_pP.LiqEtlp_pP(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
	elif tray==4:
		return triHPCThermo.HPCAllTrays4CstmLiqEtlp_pP.LiqEtlp_pP(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
	elif tray==5:
		return triHPCThermo.HPCAllTrays5CstmLiqEtlp_pP.LiqEtlp_pP(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
	elif tray==6:
		return triHPCThermo.HPCAllTrays6CstmLiqEtlp_pP.LiqEtlp_pP(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
	elif tray==7:
		return triHPCThermo.HPCAllTrays7CstmLiqEtlp_pP.LiqEtlp_pP(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
	elif tray==8:
		return triHPCThermo.HPCAllTrays8CstmLiqEtlp_pP.LiqEtlp_pP(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
	elif tray==9:
		return triHPCThermo.HPCAllTrays9CstmLiqEtlp_pP.LiqEtlp_pP(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
	elif tray==10:
		return triHPCThermo.HPCAllTrays10CstmLiqEtlp_pP.LiqEtlp_pP(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
	elif tray==11:
		return triHPCThermo.HPCAllTrays11CstmLiqEtlp_pP.LiqEtlp_pP(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
	elif tray==12:
		return triHPCThermo.HPCAllTrays12CstmLiqEtlp_pP.LiqEtlp_pP(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
	elif tray==13:
		return triHPCThermo.HPCAllTrays13CstmLiqEtlp_pP.LiqEtlp_pP(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
	elif tray==14:
		return triHPCThermo.HPCAllTrays14CstmLiqEtlp_pP.LiqEtlp_pP(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
	elif tray==15:
		return triHPCThermo.HPCAllTrays15CstmLiqEtlp_pP.LiqEtlp_pP(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
	elif tray==16:
		return triHPCThermo.HPCAllTrays16CstmLiqEtlp_pP.LiqEtlp_pP(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
	elif tray==17:
		return triHPCThermo.HPCAllTrays17CstmLiqEtlp_pP.LiqEtlp_pP(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
	elif tray==18:
		return triHPCThermo.HPCAllTrays18CstmLiqEtlp_pP.LiqEtlp_pP(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
	elif tray==19:
		return triHPCThermo.HPCAllTrays19CstmLiqEtlp_pP.LiqEtlp_pP(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
	elif tray==20:
		return triHPCThermo.HPCAllTrays20CstmLiqEtlp_pP.LiqEtlp_pP(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
	elif tray==21:
		return triHPCThermo.HPCAllTrays21CstmLiqEtlp_pP.LiqEtlp_pP(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
	elif tray==22:
		return triHPCThermo.HPCAllTrays22CstmLiqEtlp_pP.LiqEtlp_pP(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
	elif tray==23:
		return triHPCThermo.HPCAllTrays23CstmLiqEtlp_pP.LiqEtlp_pP(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
	elif tray==24:
		return triHPCThermo.HPCAllTrays24CstmLiqEtlp_pP.LiqEtlp_pP(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
	elif tray==25:
		return triHPCThermo.HPCAllTrays25CstmLiqEtlp_pP.LiqEtlp_pP(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
	elif tray==26:
		return triHPCThermo.HPCAllTrays26CstmLiqEtlp_pP.LiqEtlp_pP(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
	elif tray==27:
		return triHPCThermo.HPCAllTrays27CstmLiqEtlp_pP.LiqEtlp_pP(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
	elif tray==28:
		return triHPCThermo.HPCAllTrays28CstmLiqEtlp_pP.LiqEtlp_pP(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
	elif tray==29:
		return triHPCThermo.HPCAllTrays29CstmLiqEtlp_pP.LiqEtlp_pP(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
	elif tray==30:
		return triHPCThermo.HPCAllTrays30CstmLiqEtlp_pP.LiqEtlp_pP(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
	elif tray==31:
		return triHPCThermo.HPCAllTrays31CstmLiqEtlp_pP.LiqEtlp_pP(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
	elif tray==32:
		return triHPCThermo.HPCAllTrays32CstmLiqEtlp_pP.LiqEtlp_pP(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
	elif tray==33:
		return triHPCThermo.HPCAllTrays33CstmLiqEtlp_pP.LiqEtlp_pP(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
	elif tray==34:
		return triHPCThermo.HPCAllTrays34CstmLiqEtlp_pP.LiqEtlp_pP(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
	elif tray==35:
		return triHPCThermo.HPCAllTrays35CstmLiqEtlp_pP.LiqEtlp_pP(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
	elif tray==36:
		return triHPCThermo.HPCAllTrays36CstmLiqEtlp_pP.LiqEtlp_pP(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
	elif tray==37:
		return triHPCThermo.HPCAllTrays37CstmLiqEtlp_pP.LiqEtlp_pP(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
	elif tray==38:
		return triHPCThermo.HPCAllTrays38CstmLiqEtlp_pP.LiqEtlp_pP(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
	elif tray==39:
		return triHPCThermo.HPCAllTrays39CstmLiqEtlp_pP.LiqEtlp_pP(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
	elif tray==40:
		return triHPCThermo.HPCAllTrays40CstmLiqEtlp_pP.LiqEtlp_pP(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
	elif tray==41:
		return triHPCThermo.HPCAllTrays41CstmLiqEtlp_pP.LiqEtlp_pP(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
	elif tray==42:
		return triHPCThermo.HPCAllTrays42CstmLiqEtlp_pP.LiqEtlp_pP(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
test_model.HPCPPTrayMEtlpHldp = Expression(test_model.Time,test_model.HPCTrays,rule=HPCPPTrayMEtlpHldp)
def HPCPxTrayMEtlpHldp(m,time,tray, comp):
	if tray==1:
		if comp == 'Nitrogen':
			return triHPCThermo.HPCAllTrays1CstmLiqEtlp_px_N2.LiqEtlp_px_N2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
		else:
			return 0
	elif tray==2:
		if comp == 'Nitrogen':
			return triHPCThermo.HPCAllTrays2CstmLiqEtlp_px_N2.LiqEtlp_px_N2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
		else:
			return 0
	elif tray==3:
		if comp == 'Nitrogen':
			return triHPCThermo.HPCAllTrays3CstmLiqEtlp_px_N2.LiqEtlp_px_N2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
		else:
			return 0
	elif tray==4:
		if comp == 'Nitrogen':
			return triHPCThermo.HPCAllTrays4CstmLiqEtlp_px_N2.LiqEtlp_px_N2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
		else:
			return 0
	elif tray==5:
		if comp == 'Nitrogen':
			return triHPCThermo.HPCAllTrays5CstmLiqEtlp_px_N2.LiqEtlp_px_N2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
		else:
			return 0
	elif tray==6:
		if comp == 'Nitrogen':
			return triHPCThermo.HPCAllTrays6CstmLiqEtlp_px_N2.LiqEtlp_px_N2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
		else:
			return 0
	elif tray==7:
		if comp == 'Nitrogen':
			return triHPCThermo.HPCAllTrays7CstmLiqEtlp_px_N2.LiqEtlp_px_N2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
		else:
			return 0
	elif tray==8:
		if comp == 'Nitrogen':
			return triHPCThermo.HPCAllTrays8CstmLiqEtlp_px_N2.LiqEtlp_px_N2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
		else:
			return 0
	elif tray==9:
		if comp == 'Nitrogen':
			return triHPCThermo.HPCAllTrays9CstmLiqEtlp_px_N2.LiqEtlp_px_N2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
		else:
			return 0
	elif tray==10:
		if comp == 'Nitrogen':
			return triHPCThermo.HPCAllTrays10CstmLiqEtlp_px_N2.LiqEtlp_px_N2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
		else:
			return 0
	elif tray==11:
		if comp == 'Nitrogen':
			return triHPCThermo.HPCAllTrays11CstmLiqEtlp_px_N2.LiqEtlp_px_N2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
		else:
			return 0
	elif tray==12:
		if comp == 'Nitrogen':
			return triHPCThermo.HPCAllTrays12CstmLiqEtlp_px_N2.LiqEtlp_px_N2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
		else:
			return 0
	elif tray==13:
		if comp == 'Nitrogen':
			return triHPCThermo.HPCAllTrays13CstmLiqEtlp_px_N2.LiqEtlp_px_N2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
		else:
			return 0
	elif tray==14:
		if comp == 'Nitrogen':
			return triHPCThermo.HPCAllTrays14CstmLiqEtlp_px_N2.LiqEtlp_px_N2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
		else:
			return 0
	elif tray==15:
		if comp == 'Nitrogen':
			return triHPCThermo.HPCAllTrays15CstmLiqEtlp_px_N2.LiqEtlp_px_N2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
		else:
			return 0
	elif tray==16:
		if comp == 'Nitrogen':
			return triHPCThermo.HPCAllTrays16CstmLiqEtlp_px_N2.LiqEtlp_px_N2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
		else:
			return 0
	elif tray==17:
		if comp == 'Nitrogen':
			return triHPCThermo.HPCAllTrays17CstmLiqEtlp_px_N2.LiqEtlp_px_N2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
		else:
			return 0
	elif tray==18:
		if comp == 'Nitrogen':
			return triHPCThermo.HPCAllTrays18CstmLiqEtlp_px_N2.LiqEtlp_px_N2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
		else:
			return 0
	elif tray==19:
		if comp == 'Nitrogen':
			return triHPCThermo.HPCAllTrays19CstmLiqEtlp_px_N2.LiqEtlp_px_N2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
		else:
			return 0
	elif tray==20:
		if comp == 'Nitrogen':
			return triHPCThermo.HPCAllTrays20CstmLiqEtlp_px_N2.LiqEtlp_px_N2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
		else:
			return 0
	elif tray==21:
		if comp == 'Nitrogen':
			return triHPCThermo.HPCAllTrays21CstmLiqEtlp_px_N2.LiqEtlp_px_N2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
		else:
			return 0
	elif tray==22:
		if comp == 'Nitrogen':
			return triHPCThermo.HPCAllTrays22CstmLiqEtlp_px_N2.LiqEtlp_px_N2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
		else:
			return 0
	elif tray==23:
		if comp == 'Nitrogen':
			return triHPCThermo.HPCAllTrays23CstmLiqEtlp_px_N2.LiqEtlp_px_N2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
		else:
			return 0
	elif tray==24:
		if comp == 'Nitrogen':
			return triHPCThermo.HPCAllTrays24CstmLiqEtlp_px_N2.LiqEtlp_px_N2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
		else:
			return 0
	elif tray==25:
		if comp == 'Nitrogen':
			return triHPCThermo.HPCAllTrays25CstmLiqEtlp_px_N2.LiqEtlp_px_N2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
		else:
			return 0
	elif tray==26:
		if comp == 'Nitrogen':
			return triHPCThermo.HPCAllTrays26CstmLiqEtlp_px_N2.LiqEtlp_px_N2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
		else:
			return 0
	elif tray==27:
		if comp == 'Nitrogen':
			return triHPCThermo.HPCAllTrays27CstmLiqEtlp_px_N2.LiqEtlp_px_N2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
		else:
			return 0
	elif tray==28:
		if comp == 'Nitrogen':
			return triHPCThermo.HPCAllTrays28CstmLiqEtlp_px_N2.LiqEtlp_px_N2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
		else:
			return 0
	elif tray==29:
		if comp == 'Nitrogen':
			return triHPCThermo.HPCAllTrays29CstmLiqEtlp_px_N2.LiqEtlp_px_N2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
		else:
			return 0
	elif tray==30:
		if comp == 'Nitrogen':
			return triHPCThermo.HPCAllTrays30CstmLiqEtlp_px_N2.LiqEtlp_px_N2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
		else:
			return 0
	elif tray==31:
		if comp == 'Nitrogen':
			return triHPCThermo.HPCAllTrays31CstmLiqEtlp_px_N2.LiqEtlp_px_N2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
		else:
			return 0
	elif tray==32:
		if comp == 'Nitrogen':
			return triHPCThermo.HPCAllTrays32CstmLiqEtlp_px_N2.LiqEtlp_px_N2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
		else:
			return 0
	elif tray==33:
		if comp == 'Nitrogen':
			return triHPCThermo.HPCAllTrays33CstmLiqEtlp_px_N2.LiqEtlp_px_N2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
		else:
			return 0
	elif tray==34:
		if comp == 'Nitrogen':
			return triHPCThermo.HPCAllTrays34CstmLiqEtlp_px_N2.LiqEtlp_px_N2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
		else:
			return 0
	elif tray==35:
		if comp == 'Nitrogen':
			return triHPCThermo.HPCAllTrays35CstmLiqEtlp_px_N2.LiqEtlp_px_N2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
		else:
			return 0
	elif tray==36:
		if comp == 'Nitrogen':
			return triHPCThermo.HPCAllTrays36CstmLiqEtlp_px_N2.LiqEtlp_px_N2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
		else:
			return 0
	elif tray==37:
		if comp == 'Nitrogen':
			return triHPCThermo.HPCAllTrays37CstmLiqEtlp_px_N2.LiqEtlp_px_N2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
		else:
			return 0
	elif tray==38:
		if comp == 'Nitrogen':
			return triHPCThermo.HPCAllTrays38CstmLiqEtlp_px_N2.LiqEtlp_px_N2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
		else:
			return 0
	elif tray==39:
		if comp == 'Nitrogen':
			return triHPCThermo.HPCAllTrays39CstmLiqEtlp_px_N2.LiqEtlp_px_N2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
		else:
			return 0
	elif tray==40:
		if comp == 'Nitrogen':
			return triHPCThermo.HPCAllTrays40CstmLiqEtlp_px_N2.LiqEtlp_px_N2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
		else:
			return 0
	elif tray==41:
		if comp == 'Nitrogen':
			return triHPCThermo.HPCAllTrays41CstmLiqEtlp_px_N2.LiqEtlp_px_N2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
		else:
			return 0
	elif tray==42:
		if comp == 'Nitrogen':
			return triHPCThermo.HPCAllTrays42CstmLiqEtlp_px_N2.LiqEtlp_px_N2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) 
		else:
			return 0
test_model.HPCPxTrayMEtlpHldp = Expression(test_model.Time,test_model.HPCTrays,test_model.Component, rule=HPCPxTrayMEtlpHldp)
def HPCDtTrayTemp(m,time,tray):
	if tray==1:
		return (m.HPCDtLiqLvMFrac[time,tray,"Oxygen"] - triHPCThermo.HPCAllTrays1CstmLiqO2_pP.LiqO2_pP(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) *m.HPCDtTrayPressure[time,tray]\
    - triHPCThermo.HPCAllTrays1CstmLiqO2_px_N2.LiqO2_px_N2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) *m.HPCDtLiqLvMFrac[time,tray,"Nitrogen"]) /\
    triHPCThermo.HPCAllTrays1CstmLiqO2_pT.LiqO2_pT(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==2:
		return (m.HPCDtLiqLvMFrac[time,tray,"Oxygen"] - triHPCThermo.HPCAllTrays2CstmLiqO2_pP.LiqO2_pP(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) *m.HPCDtTrayPressure[time,tray]\
    - triHPCThermo.HPCAllTrays2CstmLiqO2_px_N2.LiqO2_px_N2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) *m.HPCDtLiqLvMFrac[time,tray,"Nitrogen"]) /\
    triHPCThermo.HPCAllTrays2CstmLiqO2_pT.LiqO2_pT(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==3:
		return (m.HPCDtLiqLvMFrac[time,tray,"Oxygen"] - triHPCThermo.HPCAllTrays3CstmLiqO2_pP.LiqO2_pP(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) *m.HPCDtTrayPressure[time,tray]\
    - triHPCThermo.HPCAllTrays3CstmLiqO2_px_N2.LiqO2_px_N2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) *m.HPCDtLiqLvMFrac[time,tray,"Nitrogen"]) /\
    triHPCThermo.HPCAllTrays3CstmLiqO2_pT.LiqO2_pT(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==4:
		return (m.HPCDtLiqLvMFrac[time,tray,"Oxygen"] - triHPCThermo.HPCAllTrays4CstmLiqO2_pP.LiqO2_pP(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) *m.HPCDtTrayPressure[time,tray]\
    - triHPCThermo.HPCAllTrays4CstmLiqO2_px_N2.LiqO2_px_N2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) *m.HPCDtLiqLvMFrac[time,tray,"Nitrogen"]) /\
    triHPCThermo.HPCAllTrays4CstmLiqO2_pT.LiqO2_pT(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==5:
		return (m.HPCDtLiqLvMFrac[time,tray,"Oxygen"] - triHPCThermo.HPCAllTrays5CstmLiqO2_pP.LiqO2_pP(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) *m.HPCDtTrayPressure[time,tray]\
    - triHPCThermo.HPCAllTrays5CstmLiqO2_px_N2.LiqO2_px_N2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) *m.HPCDtLiqLvMFrac[time,tray,"Nitrogen"]) /\
    triHPCThermo.HPCAllTrays5CstmLiqO2_pT.LiqO2_pT(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==6:
		return (m.HPCDtLiqLvMFrac[time,tray,"Oxygen"] - triHPCThermo.HPCAllTrays6CstmLiqO2_pP.LiqO2_pP(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) *m.HPCDtTrayPressure[time,tray]\
    - triHPCThermo.HPCAllTrays6CstmLiqO2_px_N2.LiqO2_px_N2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) *m.HPCDtLiqLvMFrac[time,tray,"Nitrogen"]) /\
    triHPCThermo.HPCAllTrays6CstmLiqO2_pT.LiqO2_pT(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==7:
		return (m.HPCDtLiqLvMFrac[time,tray,"Oxygen"] - triHPCThermo.HPCAllTrays7CstmLiqO2_pP.LiqO2_pP(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) *m.HPCDtTrayPressure[time,tray]\
    - triHPCThermo.HPCAllTrays7CstmLiqO2_px_N2.LiqO2_px_N2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) *m.HPCDtLiqLvMFrac[time,tray,"Nitrogen"]) /\
    triHPCThermo.HPCAllTrays7CstmLiqO2_pT.LiqO2_pT(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==8:
		return (m.HPCDtLiqLvMFrac[time,tray,"Oxygen"] - triHPCThermo.HPCAllTrays8CstmLiqO2_pP.LiqO2_pP(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) *m.HPCDtTrayPressure[time,tray]\
    - triHPCThermo.HPCAllTrays8CstmLiqO2_px_N2.LiqO2_px_N2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) *m.HPCDtLiqLvMFrac[time,tray,"Nitrogen"]) /\
    triHPCThermo.HPCAllTrays8CstmLiqO2_pT.LiqO2_pT(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==9:
		return (m.HPCDtLiqLvMFrac[time,tray,"Oxygen"] - triHPCThermo.HPCAllTrays9CstmLiqO2_pP.LiqO2_pP(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) *m.HPCDtTrayPressure[time,tray]\
    - triHPCThermo.HPCAllTrays9CstmLiqO2_px_N2.LiqO2_px_N2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) *m.HPCDtLiqLvMFrac[time,tray,"Nitrogen"]) /\
    triHPCThermo.HPCAllTrays9CstmLiqO2_pT.LiqO2_pT(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==10:
		return (m.HPCDtLiqLvMFrac[time,tray,"Oxygen"] - triHPCThermo.HPCAllTrays10CstmLiqO2_pP.LiqO2_pP(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) *m.HPCDtTrayPressure[time,tray]\
    - triHPCThermo.HPCAllTrays10CstmLiqO2_px_N2.LiqO2_px_N2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) *m.HPCDtLiqLvMFrac[time,tray,"Nitrogen"]) /\
    triHPCThermo.HPCAllTrays10CstmLiqO2_pT.LiqO2_pT(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==11:
		return (m.HPCDtLiqLvMFrac[time,tray,"Oxygen"] - triHPCThermo.HPCAllTrays11CstmLiqO2_pP.LiqO2_pP(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) *m.HPCDtTrayPressure[time,tray]\
    - triHPCThermo.HPCAllTrays11CstmLiqO2_px_N2.LiqO2_px_N2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) *m.HPCDtLiqLvMFrac[time,tray,"Nitrogen"]) /\
    triHPCThermo.HPCAllTrays11CstmLiqO2_pT.LiqO2_pT(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==12:
		return (m.HPCDtLiqLvMFrac[time,tray,"Oxygen"] - triHPCThermo.HPCAllTrays12CstmLiqO2_pP.LiqO2_pP(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) *m.HPCDtTrayPressure[time,tray]\
    - triHPCThermo.HPCAllTrays12CstmLiqO2_px_N2.LiqO2_px_N2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) *m.HPCDtLiqLvMFrac[time,tray,"Nitrogen"]) /\
    triHPCThermo.HPCAllTrays12CstmLiqO2_pT.LiqO2_pT(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==13:
		return (m.HPCDtLiqLvMFrac[time,tray,"Oxygen"] - triHPCThermo.HPCAllTrays13CstmLiqO2_pP.LiqO2_pP(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) *m.HPCDtTrayPressure[time,tray]\
    - triHPCThermo.HPCAllTrays13CstmLiqO2_px_N2.LiqO2_px_N2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) *m.HPCDtLiqLvMFrac[time,tray,"Nitrogen"]) /\
    triHPCThermo.HPCAllTrays13CstmLiqO2_pT.LiqO2_pT(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==14:
		return (m.HPCDtLiqLvMFrac[time,tray,"Oxygen"] - triHPCThermo.HPCAllTrays14CstmLiqO2_pP.LiqO2_pP(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) *m.HPCDtTrayPressure[time,tray]\
    - triHPCThermo.HPCAllTrays14CstmLiqO2_px_N2.LiqO2_px_N2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) *m.HPCDtLiqLvMFrac[time,tray,"Nitrogen"]) /\
    triHPCThermo.HPCAllTrays14CstmLiqO2_pT.LiqO2_pT(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==15:
		return (m.HPCDtLiqLvMFrac[time,tray,"Oxygen"] - triHPCThermo.HPCAllTrays15CstmLiqO2_pP.LiqO2_pP(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) *m.HPCDtTrayPressure[time,tray]\
    - triHPCThermo.HPCAllTrays15CstmLiqO2_px_N2.LiqO2_px_N2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) *m.HPCDtLiqLvMFrac[time,tray,"Nitrogen"]) /\
    triHPCThermo.HPCAllTrays15CstmLiqO2_pT.LiqO2_pT(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==16:
		return (m.HPCDtLiqLvMFrac[time,tray,"Oxygen"] - triHPCThermo.HPCAllTrays16CstmLiqO2_pP.LiqO2_pP(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) *m.HPCDtTrayPressure[time,tray]\
    - triHPCThermo.HPCAllTrays16CstmLiqO2_px_N2.LiqO2_px_N2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) *m.HPCDtLiqLvMFrac[time,tray,"Nitrogen"]) /\
    triHPCThermo.HPCAllTrays16CstmLiqO2_pT.LiqO2_pT(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==17:
		return (m.HPCDtLiqLvMFrac[time,tray,"Oxygen"] - triHPCThermo.HPCAllTrays17CstmLiqO2_pP.LiqO2_pP(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) *m.HPCDtTrayPressure[time,tray]\
    - triHPCThermo.HPCAllTrays17CstmLiqO2_px_N2.LiqO2_px_N2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) *m.HPCDtLiqLvMFrac[time,tray,"Nitrogen"]) /\
    triHPCThermo.HPCAllTrays17CstmLiqO2_pT.LiqO2_pT(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==18:
		return (m.HPCDtLiqLvMFrac[time,tray,"Oxygen"] - triHPCThermo.HPCAllTrays18CstmLiqO2_pP.LiqO2_pP(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) *m.HPCDtTrayPressure[time,tray]\
    - triHPCThermo.HPCAllTrays18CstmLiqO2_px_N2.LiqO2_px_N2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) *m.HPCDtLiqLvMFrac[time,tray,"Nitrogen"]) /\
    triHPCThermo.HPCAllTrays18CstmLiqO2_pT.LiqO2_pT(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==19:
		return (m.HPCDtLiqLvMFrac[time,tray,"Oxygen"] - triHPCThermo.HPCAllTrays19CstmLiqO2_pP.LiqO2_pP(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) *m.HPCDtTrayPressure[time,tray]\
    - triHPCThermo.HPCAllTrays19CstmLiqO2_px_N2.LiqO2_px_N2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) *m.HPCDtLiqLvMFrac[time,tray,"Nitrogen"]) /\
    triHPCThermo.HPCAllTrays19CstmLiqO2_pT.LiqO2_pT(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==20:
		return (m.HPCDtLiqLvMFrac[time,tray,"Oxygen"] - triHPCThermo.HPCAllTrays20CstmLiqO2_pP.LiqO2_pP(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) *m.HPCDtTrayPressure[time,tray]\
    - triHPCThermo.HPCAllTrays20CstmLiqO2_px_N2.LiqO2_px_N2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) *m.HPCDtLiqLvMFrac[time,tray,"Nitrogen"]) /\
    triHPCThermo.HPCAllTrays20CstmLiqO2_pT.LiqO2_pT(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==21:
		return (m.HPCDtLiqLvMFrac[time,tray,"Oxygen"] - triHPCThermo.HPCAllTrays21CstmLiqO2_pP.LiqO2_pP(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) *m.HPCDtTrayPressure[time,tray]\
    - triHPCThermo.HPCAllTrays21CstmLiqO2_px_N2.LiqO2_px_N2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) *m.HPCDtLiqLvMFrac[time,tray,"Nitrogen"]) /\
    triHPCThermo.HPCAllTrays21CstmLiqO2_pT.LiqO2_pT(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==22:
		return (m.HPCDtLiqLvMFrac[time,tray,"Oxygen"] - triHPCThermo.HPCAllTrays22CstmLiqO2_pP.LiqO2_pP(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) *m.HPCDtTrayPressure[time,tray]\
    - triHPCThermo.HPCAllTrays22CstmLiqO2_px_N2.LiqO2_px_N2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) *m.HPCDtLiqLvMFrac[time,tray,"Nitrogen"]) /\
    triHPCThermo.HPCAllTrays22CstmLiqO2_pT.LiqO2_pT(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==23:
		return (m.HPCDtLiqLvMFrac[time,tray,"Oxygen"] - triHPCThermo.HPCAllTrays23CstmLiqO2_pP.LiqO2_pP(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) *m.HPCDtTrayPressure[time,tray]\
    - triHPCThermo.HPCAllTrays23CstmLiqO2_px_N2.LiqO2_px_N2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) *m.HPCDtLiqLvMFrac[time,tray,"Nitrogen"]) /\
    triHPCThermo.HPCAllTrays23CstmLiqO2_pT.LiqO2_pT(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==24:
		return (m.HPCDtLiqLvMFrac[time,tray,"Oxygen"] - triHPCThermo.HPCAllTrays24CstmLiqO2_pP.LiqO2_pP(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) *m.HPCDtTrayPressure[time,tray]\
    - triHPCThermo.HPCAllTrays24CstmLiqO2_px_N2.LiqO2_px_N2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) *m.HPCDtLiqLvMFrac[time,tray,"Nitrogen"]) /\
    triHPCThermo.HPCAllTrays24CstmLiqO2_pT.LiqO2_pT(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==25:
		return (m.HPCDtLiqLvMFrac[time,tray,"Oxygen"] - triHPCThermo.HPCAllTrays25CstmLiqO2_pP.LiqO2_pP(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) *m.HPCDtTrayPressure[time,tray]\
    - triHPCThermo.HPCAllTrays25CstmLiqO2_px_N2.LiqO2_px_N2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) *m.HPCDtLiqLvMFrac[time,tray,"Nitrogen"]) /\
    triHPCThermo.HPCAllTrays25CstmLiqO2_pT.LiqO2_pT(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==26:
		return (m.HPCDtLiqLvMFrac[time,tray,"Oxygen"] - triHPCThermo.HPCAllTrays26CstmLiqO2_pP.LiqO2_pP(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) *m.HPCDtTrayPressure[time,tray]\
    - triHPCThermo.HPCAllTrays26CstmLiqO2_px_N2.LiqO2_px_N2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) *m.HPCDtLiqLvMFrac[time,tray,"Nitrogen"]) /\
    triHPCThermo.HPCAllTrays26CstmLiqO2_pT.LiqO2_pT(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==27:
		return (m.HPCDtLiqLvMFrac[time,tray,"Oxygen"] - triHPCThermo.HPCAllTrays27CstmLiqO2_pP.LiqO2_pP(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) *m.HPCDtTrayPressure[time,tray]\
    - triHPCThermo.HPCAllTrays27CstmLiqO2_px_N2.LiqO2_px_N2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) *m.HPCDtLiqLvMFrac[time,tray,"Nitrogen"]) /\
    triHPCThermo.HPCAllTrays27CstmLiqO2_pT.LiqO2_pT(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==28:
		return (m.HPCDtLiqLvMFrac[time,tray,"Oxygen"] - triHPCThermo.HPCAllTrays28CstmLiqO2_pP.LiqO2_pP(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) *m.HPCDtTrayPressure[time,tray]\
    - triHPCThermo.HPCAllTrays28CstmLiqO2_px_N2.LiqO2_px_N2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) *m.HPCDtLiqLvMFrac[time,tray,"Nitrogen"]) /\
    triHPCThermo.HPCAllTrays28CstmLiqO2_pT.LiqO2_pT(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==29:
		return (m.HPCDtLiqLvMFrac[time,tray,"Oxygen"] - triHPCThermo.HPCAllTrays29CstmLiqO2_pP.LiqO2_pP(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) *m.HPCDtTrayPressure[time,tray]\
    - triHPCThermo.HPCAllTrays29CstmLiqO2_px_N2.LiqO2_px_N2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) *m.HPCDtLiqLvMFrac[time,tray,"Nitrogen"]) /\
    triHPCThermo.HPCAllTrays29CstmLiqO2_pT.LiqO2_pT(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==30:
		return (m.HPCDtLiqLvMFrac[time,tray,"Oxygen"] - triHPCThermo.HPCAllTrays30CstmLiqO2_pP.LiqO2_pP(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) *m.HPCDtTrayPressure[time,tray]\
    - triHPCThermo.HPCAllTrays30CstmLiqO2_px_N2.LiqO2_px_N2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) *m.HPCDtLiqLvMFrac[time,tray,"Nitrogen"]) /\
    triHPCThermo.HPCAllTrays30CstmLiqO2_pT.LiqO2_pT(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==31:
		return (m.HPCDtLiqLvMFrac[time,tray,"Oxygen"] - triHPCThermo.HPCAllTrays31CstmLiqO2_pP.LiqO2_pP(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) *m.HPCDtTrayPressure[time,tray]\
    - triHPCThermo.HPCAllTrays31CstmLiqO2_px_N2.LiqO2_px_N2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) *m.HPCDtLiqLvMFrac[time,tray,"Nitrogen"]) /\
    triHPCThermo.HPCAllTrays31CstmLiqO2_pT.LiqO2_pT(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==32:
		return (m.HPCDtLiqLvMFrac[time,tray,"Oxygen"] - triHPCThermo.HPCAllTrays32CstmLiqO2_pP.LiqO2_pP(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) *m.HPCDtTrayPressure[time,tray]\
    - triHPCThermo.HPCAllTrays32CstmLiqO2_px_N2.LiqO2_px_N2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) *m.HPCDtLiqLvMFrac[time,tray,"Nitrogen"]) /\
    triHPCThermo.HPCAllTrays32CstmLiqO2_pT.LiqO2_pT(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==33:
		return (m.HPCDtLiqLvMFrac[time,tray,"Oxygen"] - triHPCThermo.HPCAllTrays33CstmLiqO2_pP.LiqO2_pP(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) *m.HPCDtTrayPressure[time,tray]\
    - triHPCThermo.HPCAllTrays33CstmLiqO2_px_N2.LiqO2_px_N2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) *m.HPCDtLiqLvMFrac[time,tray,"Nitrogen"]) /\
    triHPCThermo.HPCAllTrays33CstmLiqO2_pT.LiqO2_pT(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==34:
		return (m.HPCDtLiqLvMFrac[time,tray,"Oxygen"] - triHPCThermo.HPCAllTrays34CstmLiqO2_pP.LiqO2_pP(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) *m.HPCDtTrayPressure[time,tray]\
    - triHPCThermo.HPCAllTrays34CstmLiqO2_px_N2.LiqO2_px_N2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) *m.HPCDtLiqLvMFrac[time,tray,"Nitrogen"]) /\
    triHPCThermo.HPCAllTrays34CstmLiqO2_pT.LiqO2_pT(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==35:
		return (m.HPCDtLiqLvMFrac[time,tray,"Oxygen"] - triHPCThermo.HPCAllTrays35CstmLiqO2_pP.LiqO2_pP(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) *m.HPCDtTrayPressure[time,tray]\
    - triHPCThermo.HPCAllTrays35CstmLiqO2_px_N2.LiqO2_px_N2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) *m.HPCDtLiqLvMFrac[time,tray,"Nitrogen"]) /\
    triHPCThermo.HPCAllTrays35CstmLiqO2_pT.LiqO2_pT(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==36:
		return (m.HPCDtLiqLvMFrac[time,tray,"Oxygen"] - triHPCThermo.HPCAllTrays36CstmLiqO2_pP.LiqO2_pP(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) *m.HPCDtTrayPressure[time,tray]\
    - triHPCThermo.HPCAllTrays36CstmLiqO2_px_N2.LiqO2_px_N2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) *m.HPCDtLiqLvMFrac[time,tray,"Nitrogen"]) /\
    triHPCThermo.HPCAllTrays36CstmLiqO2_pT.LiqO2_pT(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==37:
		return (m.HPCDtLiqLvMFrac[time,tray,"Oxygen"] - triHPCThermo.HPCAllTrays37CstmLiqO2_pP.LiqO2_pP(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) *m.HPCDtTrayPressure[time,tray]\
    - triHPCThermo.HPCAllTrays37CstmLiqO2_px_N2.LiqO2_px_N2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) *m.HPCDtLiqLvMFrac[time,tray,"Nitrogen"]) /\
    triHPCThermo.HPCAllTrays37CstmLiqO2_pT.LiqO2_pT(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==38:
		return (m.HPCDtLiqLvMFrac[time,tray,"Oxygen"] - triHPCThermo.HPCAllTrays38CstmLiqO2_pP.LiqO2_pP(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) *m.HPCDtTrayPressure[time,tray]\
    - triHPCThermo.HPCAllTrays38CstmLiqO2_px_N2.LiqO2_px_N2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) *m.HPCDtLiqLvMFrac[time,tray,"Nitrogen"]) /\
    triHPCThermo.HPCAllTrays38CstmLiqO2_pT.LiqO2_pT(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==39:
		return (m.HPCDtLiqLvMFrac[time,tray,"Oxygen"] - triHPCThermo.HPCAllTrays39CstmLiqO2_pP.LiqO2_pP(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) *m.HPCDtTrayPressure[time,tray]\
    - triHPCThermo.HPCAllTrays39CstmLiqO2_px_N2.LiqO2_px_N2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) *m.HPCDtLiqLvMFrac[time,tray,"Nitrogen"]) /\
    triHPCThermo.HPCAllTrays39CstmLiqO2_pT.LiqO2_pT(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==40:
		return (m.HPCDtLiqLvMFrac[time,tray,"Oxygen"] - triHPCThermo.HPCAllTrays40CstmLiqO2_pP.LiqO2_pP(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) *m.HPCDtTrayPressure[time,tray]\
    - triHPCThermo.HPCAllTrays40CstmLiqO2_px_N2.LiqO2_px_N2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) *m.HPCDtLiqLvMFrac[time,tray,"Nitrogen"]) /\
    triHPCThermo.HPCAllTrays40CstmLiqO2_pT.LiqO2_pT(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==41:
		return (m.HPCDtLiqLvMFrac[time,tray,"Oxygen"] - triHPCThermo.HPCAllTrays41CstmLiqO2_pP.LiqO2_pP(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) *m.HPCDtTrayPressure[time,tray]\
    - triHPCThermo.HPCAllTrays41CstmLiqO2_px_N2.LiqO2_px_N2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) *m.HPCDtLiqLvMFrac[time,tray,"Nitrogen"]) /\
    triHPCThermo.HPCAllTrays41CstmLiqO2_pT.LiqO2_pT(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==42:
		return (m.HPCDtLiqLvMFrac[time,tray,"Oxygen"] - triHPCThermo.HPCAllTrays42CstmLiqO2_pP.LiqO2_pP(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) *m.HPCDtTrayPressure[time,tray]\
    - triHPCThermo.HPCAllTrays42CstmLiqO2_px_N2.LiqO2_px_N2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"]) *m.HPCDtLiqLvMFrac[time,tray,"Nitrogen"]) /\
    triHPCThermo.HPCAllTrays42CstmLiqO2_pT.LiqO2_pT(m.HPCTrayPressure[time,tray], m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
test_model.HPCDtTrayTemp = Expression(test_model.Time,test_model.HPCTrays,rule=HPCDtTrayTemp)
#--------HPCSump Thermo and Enthalpy---------
def HPCSumpOutMEtlp(m,time):
	return triHPCThermo.HPCSumpHdlpCstmLiqEtlp.LiqEtlp(m.HPCTrayPressure[time,1], m.HPCTrayTemp[time,1],m.HPCSumpHldpMFrac[time,"Nitrogen"])
test_model.HPCSumpOutMEtlp = Expression(test_model.Time,rule=HPCSumpOutMEtlp)
#--------HPCCond Enthalpy---------
def HPCCondOutMEtlp(m,time):
	return triHPCThermo.HPCCondOutletCstmLiqEtlp.LiqEtlp(m.HPCTrayPressure[time,42], m.HPCCondTemp[time],m.HPCVapLvMFrac[time,42,"Nitrogen"])
test_model.HPCCondOutMEtlp = Expression(test_model.Time,rule=HPCCondOutMEtlp)

#===================================
#
#         Constraints
#
#===================================

#----------------------------------
#           HPCFeed1
#----------------------------------
#--------HPCFeed1 Mass Balance---------
def HPCFeed1MassBlnc0(m, time):
	return m.HPCFeed1VF[time] * m.HPCFeed1VapMFrac[time, 'Nitrogen'] + \
(1 - m.HPCFeed1VF[time])*m.HPCFeed1LiqMFrac[time, 'Nitrogen'] - m.HPCFeed1MFrac[time, 'Nitrogen'] == 0
test_model.HPCFeed1MassBlnc0 = Constraint(test_model.Time, rule=HPCFeed1MassBlnc0)
def HPCFeed1MassBlnc1(m, time):
	return m.HPCFeed1VF[time] * m.HPCFeed1VapMFrac[time, 'Oxygen'] + \
(1 - m.HPCFeed1VF[time])*m.HPCFeed1LiqMFrac[time, 'Oxygen'] - m.HPCFeed1MFrac[time, 'Oxygen'] == 0
test_model.HPCFeed1MassBlnc1 = Constraint(test_model.Time, rule=HPCFeed1MassBlnc1)
#--------HPCFeed1 Phase Equilibrium---------
def HPCFeed1SelfLiqO2Frac(m,time):
	return m.HPCFeed1LiqMFrac[time,"Oxygen"] == triHPCThermo.HPCFeed1SelfCstmLiqO2.LiqO2(m.HPCFeed1Pressure[time],m.HPCFeed1Temp[time],m.HPCFeed1LiqMFrac[time,"Nitrogen"])
test_model.HPCFeed1SelfLiqO2Frac = Constraint(test_model.Time,rule=HPCFeed1SelfLiqO2Frac)
def HPCFeed1SelfVapO2Frac(m,time):
	return m.HPCFeed1VapMFrac[time,"Oxygen"] == triHPCThermo.HPCFeed1SelfCstmVapO2.VapO2(m.HPCFeed1Pressure[time],m.HPCFeed1Temp[time],m.HPCFeed1LiqMFrac[time,"Nitrogen"])
test_model.HPCFeed1SelfVapO2Frac = Constraint(test_model.Time,rule=HPCFeed1SelfVapO2Frac)
def HPCFeed1SelfVapN2Frac(m,time):
	return m.HPCFeed1VapMFrac[time,"Nitrogen"] == triHPCThermo.HPCFeed1SelfCstmVapN2.VapN2(m.HPCFeed1Pressure[time],m.HPCFeed1Temp[time],m.HPCFeed1LiqMFrac[time,"Nitrogen"])
test_model.HPCFeed1SelfVapN2Frac = Constraint(test_model.Time,rule=HPCFeed1SelfVapN2Frac)
#--------HPCFeed1 Summation---------
def HPCFeed1LiqSum(m, time):
	return sum([m.HPCFeed1LiqMFrac[time, c] for c in m.Component]) == 1
test_model.HPCFeed1LiqSum = Constraint(test_model.Time, rule=HPCFeed1LiqSum)
def HPCFeed1VapSum(m, time):
	return sum([m.HPCFeed1VapMFrac[time, c] for c in m.Component]) == 1
test_model.HPCFeed1VapSum = Constraint(test_model.Time, rule=HPCFeed1VapSum)

#----------------------------------
#           HPCFeed2
#----------------------------------
#--------HPCFeed2 Mass Balance---------
def HPCFeed2MassBlnc0(m, time):
	return m.HPCFeed2VF[time] * m.HPCFeed2VapMFrac[time, 'Nitrogen'] + \
(1 - m.HPCFeed2VF[time])*m.HPCFeed2LiqMFrac[time, 'Nitrogen'] - m.HPCFeed2MFrac[time, 'Nitrogen'] == 0
test_model.HPCFeed2MassBlnc0 = Constraint(test_model.Time, rule=HPCFeed2MassBlnc0)
def HPCFeed2MassBlnc1(m, time):
	return m.HPCFeed2VF[time] * m.HPCFeed2VapMFrac[time, 'Oxygen'] + \
(1 - m.HPCFeed2VF[time])*m.HPCFeed2LiqMFrac[time, 'Oxygen'] - m.HPCFeed2MFrac[time, 'Oxygen'] == 0
test_model.HPCFeed2MassBlnc1 = Constraint(test_model.Time, rule=HPCFeed2MassBlnc1)
#--------HPCFeed2 Phase Equilibrium---------
def HPCFeed2SelfLiqO2Frac(m,time):
	return m.HPCFeed2LiqMFrac[time,"Oxygen"] == triHPCThermo.HPCFeed2SelfCstmLiqO2.LiqO2(m.HPCFeed2Pressure[time],m.HPCFeed2Temp[time],m.HPCFeed2LiqMFrac[time,"Nitrogen"])
test_model.HPCFeed2SelfLiqO2Frac = Constraint(test_model.Time,rule=HPCFeed2SelfLiqO2Frac)
def HPCFeed2SelfVapO2Frac(m,time):
	return m.HPCFeed2VapMFrac[time,"Oxygen"] == triHPCThermo.HPCFeed2SelfCstmVapO2.VapO2(m.HPCFeed2Pressure[time],m.HPCFeed2Temp[time],m.HPCFeed2LiqMFrac[time,"Nitrogen"])
test_model.HPCFeed2SelfVapO2Frac = Constraint(test_model.Time,rule=HPCFeed2SelfVapO2Frac)
def HPCFeed2SelfVapN2Frac(m,time):
	return m.HPCFeed2VapMFrac[time,"Nitrogen"] == triHPCThermo.HPCFeed2SelfCstmVapN2.VapN2(m.HPCFeed2Pressure[time],m.HPCFeed2Temp[time],m.HPCFeed2LiqMFrac[time,"Nitrogen"])
test_model.HPCFeed2SelfVapN2Frac = Constraint(test_model.Time,rule=HPCFeed2SelfVapN2Frac)
#--------HPCFeed2 Summation---------
def HPCFeed2LiqSum(m, time):
	return sum([m.HPCFeed2LiqMFrac[time, c] for c in m.Component]) == 1
test_model.HPCFeed2LiqSum = Constraint(test_model.Time, rule=HPCFeed2LiqSum)
def HPCFeed2VapSum(m, time):
	return sum([m.HPCFeed2VapMFrac[time, c] for c in m.Component]) == 1
test_model.HPCFeed2VapSum = Constraint(test_model.Time, rule=HPCFeed2VapSum)

#----------------------------------
#           HPC
#----------------------------------
#--------HPC Mass Balance---------
def HPCMassBlnc(m,time, tray, comp):
	if tray == 1:
		return (m.HPCLiqLvMCompFlow[time, tray + 1, comp]- m.HPCLiqLvMCompFlow[time, tray, comp] - m.HPCVapLvMCompFlow[time, tray, comp]+m.HPCFeed1MFlow[time]*m.HPCFeed1MFrac[time, comp]-m.HPCDtTrayMCompHldp[time,tray,comp])*0.001000 == 0
	elif tray == 4:
		return (m.HPCLiqLvMCompFlow[time, tray + 1, comp] + m.HPCVapLvMCompFlow[time, tray - 1, comp] - m.HPCLiqLvMCompFlow[time, tray, comp] - m.HPCVapLvMCompFlow[time, tray, comp]+m.HPCFeed2MFlow[time]*m.HPCFeed2MFrac[time, comp]-m.HPCDtTrayMCompHldp[time,tray,comp])*0.001000 == 0
	elif tray == 6:
		return (m.HPCLiqLvMCompFlow[time, tray + 1, comp] + m.HPCVapLvMCompFlow[time, tray - 1, comp] - m.HPCLiqLvMCompFlow[time, tray, comp] - m.HPCVapLvMCompFlow[time, tray, comp]-m.HPCExt6MFlow[time]*m.HPCExt6MFrac[time, comp]-m.HPCDtTrayMCompHldp[time,tray,comp])*0.001000 == 0
	elif tray == 22:
		return (m.HPCLiqLvMCompFlow[time, tray + 1, comp] + m.HPCVapLvMCompFlow[time, tray - 1, comp] - m.HPCLiqLvMCompFlow[time, tray, comp] - m.HPCVapLvMCompFlow[time, tray, comp]-m.HPCExt22MFlow[time]*m.HPCExt22MFrac[time, comp]-m.HPCDtTrayMCompHldp[time,tray,comp])*0.001000 == 0
	elif tray == 42:
		return (m.HPCCondRefMFlow[time]*m.HPCVapLvMFrac[time,42, comp] + m.HPCVapLvMCompFlow[time, tray - 1, comp] - m.HPCLiqLvMCompFlow[time, tray, comp] - m.HPCVapLvMCompFlow[time, tray, comp]-m.HPCDtTrayMCompHldp[time,tray,comp])*0.001000 == 0
	else:
		return (m.HPCLiqLvMCompFlow[time, tray + 1, comp] + m.HPCVapLvMCompFlow[time, tray - 1, comp] - m.HPCLiqLvMCompFlow[time, tray, comp] - m.HPCVapLvMCompFlow[time, tray, comp]-m.HPCDtTrayMCompHldp[time,tray,comp])*0.001000 == 0
test_model.HPCMassBlnc = Constraint(test_model.Time, test_model.HPCTrays, test_model.Component, rule=HPCMassBlnc)
def HPCMCompHldpEqu(m, time, tray, comp):
	return (m.HPCTrayMCompHldp[time, tray, comp] - m.HPCTrayMHldp[time, tray] * m.HPCLiqLvMFrac[time, tray, comp]) * 1e-2 == 0
test_model.HPCMCompHldpEqu = Constraint(test_model.Time, test_model.HPCTrays, test_model.Component, rule=HPCMCompHldpEqu)
#--------HPC Energy Balance---------
def HPCEngBlnc(m,time,tray):
	if tray == 1:
		return (m.HPCLiqLvMFlow[time,tray + 1] * m.HPCLiqLvMEtlp[time,tray+1] \
		        - m.HPCLiqLvMFlow[time,tray] * m.HPCLiqLvMEtlp[time,tray] \
		        - m.HPCVapLvMFlow[time,tray] * m.HPCVapLvMEtlp[time,tray]\
		        +m.HPCFeed1MFlow[time]*m.HPCFeed1MEtlp[time]-m.HPCDtTrayMEtlpHldp[time,tray]-m.HPCUALeakage[time]*(m.HPCAmbientTemp[time]-m.HPCTrayTemp[time,tray]))*0.000010 == 0
	elif tray == 4:
		return (m.HPCLiqLvMFlow[time,tray + 1] * m.HPCLiqLvMEtlp[time,tray+1] \
		        + m.HPCVapLvMFlow[time,tray-1] * m.HPCVapLvMEtlp[time,tray-1] \
		        - m.HPCLiqLvMFlow[time,tray] * m.HPCLiqLvMEtlp[time,tray] \
		        - m.HPCVapLvMFlow[time,tray] * m.HPCVapLvMEtlp[time,tray]\
		        +m.HPCFeed2MFlow[time]*m.HPCFeed2MEtlp[time]-m.HPCDtTrayMEtlpHldp[time,tray]-m.HPCUALeakage[time]*(m.HPCAmbientTemp[time]-m.HPCTrayTemp[time,tray]))*0.000010 == 0
	elif tray == 6:
		return (m.HPCLiqLvMFlow[time,tray + 1] * m.HPCLiqLvMEtlp[time,tray+1] \
		        + m.HPCVapLvMFlow[time,tray-1] * m.HPCVapLvMEtlp[time,tray-1] \
		        - m.HPCLiqLvMFlow[time,tray] * m.HPCLiqLvMEtlp[time,tray] \
		        - m.HPCVapLvMFlow[time,tray] * m.HPCVapLvMEtlp[time,tray]\
		        -m.HPCExt6MFlow[time]*m.HPCExt6MEtlp[time]-m.HPCDtTrayMEtlpHldp[time,tray]-m.HPCUALeakage[time]*(m.HPCAmbientTemp[time]-m.HPCTrayTemp[time,tray]))*0.000010 == 0
	elif tray == 22:
		return (m.HPCLiqLvMFlow[time,tray + 1] * m.HPCLiqLvMEtlp[time,tray+1] \
		        + m.HPCVapLvMFlow[time,tray-1] * m.HPCVapLvMEtlp[time,tray-1] \
		        - m.HPCLiqLvMFlow[time,tray] * m.HPCLiqLvMEtlp[time,tray] \
		        - m.HPCVapLvMFlow[time,tray] * m.HPCVapLvMEtlp[time,tray]\
		        -m.HPCExt22MFlow[time]*m.HPCExt22MEtlp[time]-m.HPCDtTrayMEtlpHldp[time,tray]-m.HPCUALeakage[time]*(m.HPCAmbientTemp[time]-m.HPCTrayTemp[time,tray]))*0.000010 == 0
	elif tray == 42:
		return (m.HPCCondRefMFlow[time] * m.HPCCondOutMEtlp[time] \
		        + m.HPCVapLvMFlow[time,tray-1] * m.HPCVapLvMEtlp[time,tray-1] \
		        - m.HPCLiqLvMFlow[time,tray] * m.HPCLiqLvMEtlp[time,tray] \
		        - m.HPCVapLvMFlow[time,tray] * m.HPCVapLvMEtlp[time,tray]-m.HPCDtTrayMEtlpHldp[time,tray]-m.HPCUALeakage[time]*(m.HPCAmbientTemp[time]-m.HPCTrayTemp[time,tray]))*0.000010 == 0
	else:
		return (m.HPCLiqLvMFlow[time,tray + 1] * m.HPCLiqLvMEtlp[time,tray+1] \
		        + m.HPCVapLvMFlow[time,tray-1] * m.HPCVapLvMEtlp[time,tray-1] \
		        - m.HPCLiqLvMFlow[time,tray] * m.HPCLiqLvMEtlp[time,tray] \
		        - m.HPCVapLvMFlow[time,tray] * m.HPCVapLvMEtlp[time,tray] \
		        - m.HPCDtTrayMEtlpHldp[time,tray]-m.HPCUALeakage[time]*(m.HPCAmbientTemp[time]-m.HPCTrayTemp[time,tray]))*0.000010 == 0
test_model.HPCEngBlnc = Constraint(test_model.Time, test_model.HPCTrays,rule=HPCEngBlnc)
def HPCAllTraysMEtlpEqu(m,time,tray):
	return (m.HPCTrayMHldp[time,tray] * (m.HPCPTTrayMEtlpHldp[time,tray] * m.HPCDtTrayTemp[time,tray] + \
	      sum([m.HPCPxTrayMEtlpHldp[time, tray, c] * m.HPCDtLiqLvMFrac[time, tray, c] for c in m.Component])) + \
	      m.HPCLiqLvMEtlp[time,tray] * m.HPCDtTrayMHldp[time,tray] - m.HPCDtTrayMEtlpHldp[time,tray]) * 1e-2 == 0
test_model.HPCAllTraysMEtlpEqu = Constraint(test_model.Time,test_model.HPCTrays,rule=HPCAllTraysMEtlpEqu)
#--------HPC Phase Equilibrium & System Parts---------
def HPCAllTraysLiqO2Frac(m,time,tray):
	if tray==1:
		return m.HPCLiqLvMFrac[time,tray,"Oxygen"] == triHPCThermo.HPCAllTrays1CstmLiqO2.LiqO2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==2:
		return m.HPCLiqLvMFrac[time,tray,"Oxygen"] == triHPCThermo.HPCAllTrays2CstmLiqO2.LiqO2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==3:
		return m.HPCLiqLvMFrac[time,tray,"Oxygen"] == triHPCThermo.HPCAllTrays3CstmLiqO2.LiqO2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==4:
		return m.HPCLiqLvMFrac[time,tray,"Oxygen"] == triHPCThermo.HPCAllTrays4CstmLiqO2.LiqO2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==5:
		return m.HPCLiqLvMFrac[time,tray,"Oxygen"] == triHPCThermo.HPCAllTrays5CstmLiqO2.LiqO2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==6:
		return m.HPCLiqLvMFrac[time,tray,"Oxygen"] == triHPCThermo.HPCAllTrays6CstmLiqO2.LiqO2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==7:
		return m.HPCLiqLvMFrac[time,tray,"Oxygen"] == triHPCThermo.HPCAllTrays7CstmLiqO2.LiqO2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==8:
		return m.HPCLiqLvMFrac[time,tray,"Oxygen"] == triHPCThermo.HPCAllTrays8CstmLiqO2.LiqO2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==9:
		return m.HPCLiqLvMFrac[time,tray,"Oxygen"] == triHPCThermo.HPCAllTrays9CstmLiqO2.LiqO2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==10:
		return m.HPCLiqLvMFrac[time,tray,"Oxygen"] == triHPCThermo.HPCAllTrays10CstmLiqO2.LiqO2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==11:
		return m.HPCLiqLvMFrac[time,tray,"Oxygen"] == triHPCThermo.HPCAllTrays11CstmLiqO2.LiqO2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==12:
		return m.HPCLiqLvMFrac[time,tray,"Oxygen"] == triHPCThermo.HPCAllTrays12CstmLiqO2.LiqO2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==13:
		return m.HPCLiqLvMFrac[time,tray,"Oxygen"] == triHPCThermo.HPCAllTrays13CstmLiqO2.LiqO2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==14:
		return m.HPCLiqLvMFrac[time,tray,"Oxygen"] == triHPCThermo.HPCAllTrays14CstmLiqO2.LiqO2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==15:
		return m.HPCLiqLvMFrac[time,tray,"Oxygen"] == triHPCThermo.HPCAllTrays15CstmLiqO2.LiqO2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==16:
		return m.HPCLiqLvMFrac[time,tray,"Oxygen"] == triHPCThermo.HPCAllTrays16CstmLiqO2.LiqO2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==17:
		return m.HPCLiqLvMFrac[time,tray,"Oxygen"] == triHPCThermo.HPCAllTrays17CstmLiqO2.LiqO2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==18:
		return m.HPCLiqLvMFrac[time,tray,"Oxygen"] == triHPCThermo.HPCAllTrays18CstmLiqO2.LiqO2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==19:
		return m.HPCLiqLvMFrac[time,tray,"Oxygen"] == triHPCThermo.HPCAllTrays19CstmLiqO2.LiqO2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==20:
		return m.HPCLiqLvMFrac[time,tray,"Oxygen"] == triHPCThermo.HPCAllTrays20CstmLiqO2.LiqO2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==21:
		return m.HPCLiqLvMFrac[time,tray,"Oxygen"] == triHPCThermo.HPCAllTrays21CstmLiqO2.LiqO2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==22:
		return m.HPCLiqLvMFrac[time,tray,"Oxygen"] == triHPCThermo.HPCAllTrays22CstmLiqO2.LiqO2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==23:
		return m.HPCLiqLvMFrac[time,tray,"Oxygen"] == triHPCThermo.HPCAllTrays23CstmLiqO2.LiqO2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==24:
		return m.HPCLiqLvMFrac[time,tray,"Oxygen"] == triHPCThermo.HPCAllTrays24CstmLiqO2.LiqO2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==25:
		return m.HPCLiqLvMFrac[time,tray,"Oxygen"] == triHPCThermo.HPCAllTrays25CstmLiqO2.LiqO2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==26:
		return m.HPCLiqLvMFrac[time,tray,"Oxygen"] == triHPCThermo.HPCAllTrays26CstmLiqO2.LiqO2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==27:
		return m.HPCLiqLvMFrac[time,tray,"Oxygen"] == triHPCThermo.HPCAllTrays27CstmLiqO2.LiqO2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==28:
		return m.HPCLiqLvMFrac[time,tray,"Oxygen"] == triHPCThermo.HPCAllTrays28CstmLiqO2.LiqO2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==29:
		return m.HPCLiqLvMFrac[time,tray,"Oxygen"] == triHPCThermo.HPCAllTrays29CstmLiqO2.LiqO2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==30:
		return m.HPCLiqLvMFrac[time,tray,"Oxygen"] == triHPCThermo.HPCAllTrays30CstmLiqO2.LiqO2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==31:
		return m.HPCLiqLvMFrac[time,tray,"Oxygen"] == triHPCThermo.HPCAllTrays31CstmLiqO2.LiqO2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==32:
		return m.HPCLiqLvMFrac[time,tray,"Oxygen"] == triHPCThermo.HPCAllTrays32CstmLiqO2.LiqO2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==33:
		return m.HPCLiqLvMFrac[time,tray,"Oxygen"] == triHPCThermo.HPCAllTrays33CstmLiqO2.LiqO2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==34:
		return m.HPCLiqLvMFrac[time,tray,"Oxygen"] == triHPCThermo.HPCAllTrays34CstmLiqO2.LiqO2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==35:
		return m.HPCLiqLvMFrac[time,tray,"Oxygen"] == triHPCThermo.HPCAllTrays35CstmLiqO2.LiqO2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==36:
		return m.HPCLiqLvMFrac[time,tray,"Oxygen"] == triHPCThermo.HPCAllTrays36CstmLiqO2.LiqO2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==37:
		return m.HPCLiqLvMFrac[time,tray,"Oxygen"] == triHPCThermo.HPCAllTrays37CstmLiqO2.LiqO2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==38:
		return m.HPCLiqLvMFrac[time,tray,"Oxygen"] == triHPCThermo.HPCAllTrays38CstmLiqO2.LiqO2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==39:
		return m.HPCLiqLvMFrac[time,tray,"Oxygen"] == triHPCThermo.HPCAllTrays39CstmLiqO2.LiqO2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==40:
		return m.HPCLiqLvMFrac[time,tray,"Oxygen"] == triHPCThermo.HPCAllTrays40CstmLiqO2.LiqO2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==41:
		return m.HPCLiqLvMFrac[time,tray,"Oxygen"] == triHPCThermo.HPCAllTrays41CstmLiqO2.LiqO2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==42:
		return m.HPCLiqLvMFrac[time,tray,"Oxygen"] == triHPCThermo.HPCAllTrays42CstmLiqO2.LiqO2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
test_model.HPCAllTraysLiqO2Frac = Constraint(test_model.Time,test_model.HPCTrays,rule=HPCAllTraysLiqO2Frac)
def HPCAllTraysVapO2Frac(m,time,tray):
	if tray==1:
		return m.HPCVapLvMFrac[time,tray,"Oxygen"] == triHPCThermo.HPCAllTrays1CstmVapO2.VapO2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==2:
		return m.HPCVapLvMFrac[time,tray,"Oxygen"] == triHPCThermo.HPCAllTrays2CstmVapO2.VapO2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==3:
		return m.HPCVapLvMFrac[time,tray,"Oxygen"] == triHPCThermo.HPCAllTrays3CstmVapO2.VapO2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==4:
		return m.HPCVapLvMFrac[time,tray,"Oxygen"] == triHPCThermo.HPCAllTrays4CstmVapO2.VapO2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==5:
		return m.HPCVapLvMFrac[time,tray,"Oxygen"] == triHPCThermo.HPCAllTrays5CstmVapO2.VapO2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==6:
		return m.HPCVapLvMFrac[time,tray,"Oxygen"] == triHPCThermo.HPCAllTrays6CstmVapO2.VapO2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==7:
		return m.HPCVapLvMFrac[time,tray,"Oxygen"] == triHPCThermo.HPCAllTrays7CstmVapO2.VapO2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==8:
		return m.HPCVapLvMFrac[time,tray,"Oxygen"] == triHPCThermo.HPCAllTrays8CstmVapO2.VapO2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==9:
		return m.HPCVapLvMFrac[time,tray,"Oxygen"] == triHPCThermo.HPCAllTrays9CstmVapO2.VapO2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==10:
		return m.HPCVapLvMFrac[time,tray,"Oxygen"] == triHPCThermo.HPCAllTrays10CstmVapO2.VapO2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==11:
		return m.HPCVapLvMFrac[time,tray,"Oxygen"] == triHPCThermo.HPCAllTrays11CstmVapO2.VapO2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==12:
		return m.HPCVapLvMFrac[time,tray,"Oxygen"] == triHPCThermo.HPCAllTrays12CstmVapO2.VapO2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==13:
		return m.HPCVapLvMFrac[time,tray,"Oxygen"] == triHPCThermo.HPCAllTrays13CstmVapO2.VapO2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==14:
		return m.HPCVapLvMFrac[time,tray,"Oxygen"] == triHPCThermo.HPCAllTrays14CstmVapO2.VapO2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==15:
		return m.HPCVapLvMFrac[time,tray,"Oxygen"] == triHPCThermo.HPCAllTrays15CstmVapO2.VapO2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==16:
		return m.HPCVapLvMFrac[time,tray,"Oxygen"] == triHPCThermo.HPCAllTrays16CstmVapO2.VapO2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==17:
		return m.HPCVapLvMFrac[time,tray,"Oxygen"] == triHPCThermo.HPCAllTrays17CstmVapO2.VapO2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==18:
		return m.HPCVapLvMFrac[time,tray,"Oxygen"] == triHPCThermo.HPCAllTrays18CstmVapO2.VapO2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==19:
		return m.HPCVapLvMFrac[time,tray,"Oxygen"] == triHPCThermo.HPCAllTrays19CstmVapO2.VapO2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==20:
		return m.HPCVapLvMFrac[time,tray,"Oxygen"] == triHPCThermo.HPCAllTrays20CstmVapO2.VapO2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==21:
		return m.HPCVapLvMFrac[time,tray,"Oxygen"] == triHPCThermo.HPCAllTrays21CstmVapO2.VapO2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==22:
		return m.HPCVapLvMFrac[time,tray,"Oxygen"] == triHPCThermo.HPCAllTrays22CstmVapO2.VapO2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==23:
		return m.HPCVapLvMFrac[time,tray,"Oxygen"] == triHPCThermo.HPCAllTrays23CstmVapO2.VapO2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==24:
		return m.HPCVapLvMFrac[time,tray,"Oxygen"] == triHPCThermo.HPCAllTrays24CstmVapO2.VapO2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==25:
		return m.HPCVapLvMFrac[time,tray,"Oxygen"] == triHPCThermo.HPCAllTrays25CstmVapO2.VapO2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==26:
		return m.HPCVapLvMFrac[time,tray,"Oxygen"] == triHPCThermo.HPCAllTrays26CstmVapO2.VapO2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==27:
		return m.HPCVapLvMFrac[time,tray,"Oxygen"] == triHPCThermo.HPCAllTrays27CstmVapO2.VapO2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==28:
		return m.HPCVapLvMFrac[time,tray,"Oxygen"] == triHPCThermo.HPCAllTrays28CstmVapO2.VapO2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==29:
		return m.HPCVapLvMFrac[time,tray,"Oxygen"] == triHPCThermo.HPCAllTrays29CstmVapO2.VapO2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==30:
		return m.HPCVapLvMFrac[time,tray,"Oxygen"] == triHPCThermo.HPCAllTrays30CstmVapO2.VapO2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==31:
		return m.HPCVapLvMFrac[time,tray,"Oxygen"] == triHPCThermo.HPCAllTrays31CstmVapO2.VapO2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==32:
		return m.HPCVapLvMFrac[time,tray,"Oxygen"] == triHPCThermo.HPCAllTrays32CstmVapO2.VapO2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==33:
		return m.HPCVapLvMFrac[time,tray,"Oxygen"] == triHPCThermo.HPCAllTrays33CstmVapO2.VapO2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==34:
		return m.HPCVapLvMFrac[time,tray,"Oxygen"] == triHPCThermo.HPCAllTrays34CstmVapO2.VapO2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==35:
		return m.HPCVapLvMFrac[time,tray,"Oxygen"] == triHPCThermo.HPCAllTrays35CstmVapO2.VapO2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==36:
		return m.HPCVapLvMFrac[time,tray,"Oxygen"] == triHPCThermo.HPCAllTrays36CstmVapO2.VapO2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==37:
		return m.HPCVapLvMFrac[time,tray,"Oxygen"] == triHPCThermo.HPCAllTrays37CstmVapO2.VapO2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==38:
		return m.HPCVapLvMFrac[time,tray,"Oxygen"] == triHPCThermo.HPCAllTrays38CstmVapO2.VapO2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==39:
		return m.HPCVapLvMFrac[time,tray,"Oxygen"] == triHPCThermo.HPCAllTrays39CstmVapO2.VapO2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==40:
		return m.HPCVapLvMFrac[time,tray,"Oxygen"] == triHPCThermo.HPCAllTrays40CstmVapO2.VapO2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==41:
		return m.HPCVapLvMFrac[time,tray,"Oxygen"] == triHPCThermo.HPCAllTrays41CstmVapO2.VapO2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==42:
		return m.HPCVapLvMFrac[time,tray,"Oxygen"] == triHPCThermo.HPCAllTrays42CstmVapO2.VapO2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
test_model.HPCAllTraysVapO2Frac = Constraint(test_model.Time,test_model.HPCTrays,rule=HPCAllTraysVapO2Frac)
def HPCAllTraysVapN2Frac(m,time,tray):
	if tray==1:
		return m.HPCVapLvMFrac[time,tray,"Nitrogen"] == triHPCThermo.HPCAllTrays1CstmVapN2.VapN2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==2:
		return m.HPCVapLvMFrac[time,tray,"Nitrogen"] == triHPCThermo.HPCAllTrays2CstmVapN2.VapN2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==3:
		return m.HPCVapLvMFrac[time,tray,"Nitrogen"] == triHPCThermo.HPCAllTrays3CstmVapN2.VapN2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==4:
		return m.HPCVapLvMFrac[time,tray,"Nitrogen"] == triHPCThermo.HPCAllTrays4CstmVapN2.VapN2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==5:
		return m.HPCVapLvMFrac[time,tray,"Nitrogen"] == triHPCThermo.HPCAllTrays5CstmVapN2.VapN2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==6:
		return m.HPCVapLvMFrac[time,tray,"Nitrogen"] == triHPCThermo.HPCAllTrays6CstmVapN2.VapN2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==7:
		return m.HPCVapLvMFrac[time,tray,"Nitrogen"] == triHPCThermo.HPCAllTrays7CstmVapN2.VapN2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==8:
		return m.HPCVapLvMFrac[time,tray,"Nitrogen"] == triHPCThermo.HPCAllTrays8CstmVapN2.VapN2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==9:
		return m.HPCVapLvMFrac[time,tray,"Nitrogen"] == triHPCThermo.HPCAllTrays9CstmVapN2.VapN2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==10:
		return m.HPCVapLvMFrac[time,tray,"Nitrogen"] == triHPCThermo.HPCAllTrays10CstmVapN2.VapN2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==11:
		return m.HPCVapLvMFrac[time,tray,"Nitrogen"] == triHPCThermo.HPCAllTrays11CstmVapN2.VapN2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==12:
		return m.HPCVapLvMFrac[time,tray,"Nitrogen"] == triHPCThermo.HPCAllTrays12CstmVapN2.VapN2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==13:
		return m.HPCVapLvMFrac[time,tray,"Nitrogen"] == triHPCThermo.HPCAllTrays13CstmVapN2.VapN2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==14:
		return m.HPCVapLvMFrac[time,tray,"Nitrogen"] == triHPCThermo.HPCAllTrays14CstmVapN2.VapN2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==15:
		return m.HPCVapLvMFrac[time,tray,"Nitrogen"] == triHPCThermo.HPCAllTrays15CstmVapN2.VapN2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==16:
		return m.HPCVapLvMFrac[time,tray,"Nitrogen"] == triHPCThermo.HPCAllTrays16CstmVapN2.VapN2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==17:
		return m.HPCVapLvMFrac[time,tray,"Nitrogen"] == triHPCThermo.HPCAllTrays17CstmVapN2.VapN2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==18:
		return m.HPCVapLvMFrac[time,tray,"Nitrogen"] == triHPCThermo.HPCAllTrays18CstmVapN2.VapN2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==19:
		return m.HPCVapLvMFrac[time,tray,"Nitrogen"] == triHPCThermo.HPCAllTrays19CstmVapN2.VapN2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==20:
		return m.HPCVapLvMFrac[time,tray,"Nitrogen"] == triHPCThermo.HPCAllTrays20CstmVapN2.VapN2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==21:
		return m.HPCVapLvMFrac[time,tray,"Nitrogen"] == triHPCThermo.HPCAllTrays21CstmVapN2.VapN2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==22:
		return m.HPCVapLvMFrac[time,tray,"Nitrogen"] == triHPCThermo.HPCAllTrays22CstmVapN2.VapN2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==23:
		return m.HPCVapLvMFrac[time,tray,"Nitrogen"] == triHPCThermo.HPCAllTrays23CstmVapN2.VapN2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==24:
		return m.HPCVapLvMFrac[time,tray,"Nitrogen"] == triHPCThermo.HPCAllTrays24CstmVapN2.VapN2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==25:
		return m.HPCVapLvMFrac[time,tray,"Nitrogen"] == triHPCThermo.HPCAllTrays25CstmVapN2.VapN2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==26:
		return m.HPCVapLvMFrac[time,tray,"Nitrogen"] == triHPCThermo.HPCAllTrays26CstmVapN2.VapN2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==27:
		return m.HPCVapLvMFrac[time,tray,"Nitrogen"] == triHPCThermo.HPCAllTrays27CstmVapN2.VapN2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==28:
		return m.HPCVapLvMFrac[time,tray,"Nitrogen"] == triHPCThermo.HPCAllTrays28CstmVapN2.VapN2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==29:
		return m.HPCVapLvMFrac[time,tray,"Nitrogen"] == triHPCThermo.HPCAllTrays29CstmVapN2.VapN2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==30:
		return m.HPCVapLvMFrac[time,tray,"Nitrogen"] == triHPCThermo.HPCAllTrays30CstmVapN2.VapN2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==31:
		return m.HPCVapLvMFrac[time,tray,"Nitrogen"] == triHPCThermo.HPCAllTrays31CstmVapN2.VapN2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==32:
		return m.HPCVapLvMFrac[time,tray,"Nitrogen"] == triHPCThermo.HPCAllTrays32CstmVapN2.VapN2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==33:
		return m.HPCVapLvMFrac[time,tray,"Nitrogen"] == triHPCThermo.HPCAllTrays33CstmVapN2.VapN2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==34:
		return m.HPCVapLvMFrac[time,tray,"Nitrogen"] == triHPCThermo.HPCAllTrays34CstmVapN2.VapN2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==35:
		return m.HPCVapLvMFrac[time,tray,"Nitrogen"] == triHPCThermo.HPCAllTrays35CstmVapN2.VapN2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==36:
		return m.HPCVapLvMFrac[time,tray,"Nitrogen"] == triHPCThermo.HPCAllTrays36CstmVapN2.VapN2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==37:
		return m.HPCVapLvMFrac[time,tray,"Nitrogen"] == triHPCThermo.HPCAllTrays37CstmVapN2.VapN2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==38:
		return m.HPCVapLvMFrac[time,tray,"Nitrogen"] == triHPCThermo.HPCAllTrays38CstmVapN2.VapN2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==39:
		return m.HPCVapLvMFrac[time,tray,"Nitrogen"] == triHPCThermo.HPCAllTrays39CstmVapN2.VapN2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==40:
		return m.HPCVapLvMFrac[time,tray,"Nitrogen"] == triHPCThermo.HPCAllTrays40CstmVapN2.VapN2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==41:
		return m.HPCVapLvMFrac[time,tray,"Nitrogen"] == triHPCThermo.HPCAllTrays41CstmVapN2.VapN2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
	elif tray==42:
		return m.HPCVapLvMFrac[time,tray,"Nitrogen"] == triHPCThermo.HPCAllTrays42CstmVapN2.VapN2(m.HPCTrayPressure[time,tray],m.HPCTrayTemp[time,tray],m.HPCLiqLvMFrac[time,tray,"Nitrogen"])
test_model.HPCAllTraysVapN2Frac = Constraint(test_model.Time,test_model.HPCTrays,rule=HPCAllTraysVapN2Frac)
#--------HPC Hydraulics---------
def HPCAllTraysHydro(m,time,tray):
	return (m.HPCLiqLvMFlow[time,tray] - m.HPCAllTraysHydroParak*m.HPCTrayMHldp[time,tray])*0.001000 == 0
test_model.HPCAllTraysHydro = Constraint(test_model.Time,test_model.HPCTrays,rule=HPCAllTraysHydro)
#--------HPC Summation---------
def HPCLiqSum(m,time, tray):
	return sum([m.HPCLiqLvMFrac[time, tray, c] for c in m.Component]) == 1
test_model.HPCLiqSum = Constraint(test_model.Time, test_model.HPCTrays, rule=HPCLiqSum)
def HPCVapSum(m,time, tray):
	return sum([m.HPCVapLvMFrac[time, tray, c] for c in m.Component]) == 1
test_model.HPCVapSum = Constraint(test_model.Time, test_model.HPCTrays, rule=HPCVapSum)
#--------HPC Pressure Profile---------
def HPCPProf(m, time, tray):
	return ((m.HPCTopPressure[time]-m.HPCBtmPressure[time])/41*(tray-1)+m.HPCBtmPressure[time] - m.HPCTrayPressure[time, tray])*0.010000 == 0
test_model.HPCPProf = Constraint(test_model.Time, test_model.HPCTrays, rule=HPCPProf)
#--------HPC Extractions---------
def HPCExt6MFracSpec(m, time, comp):
	return m.HPCExt6MFrac[time, comp] - m.HPCLiqLvMFrac[time, 6, comp] == 0 
test_model.HPCExt6MFracSpec = Constraint(test_model.Time, test_model.Component, rule=HPCExt6MFracSpec)
def HPCExt6MEtlpSpec(m, time):
	return (m.HPCExt6MEtlp[time] - m.HPCLiqLvMEtlp[time, 6])*  0.000010 == 0
test_model.HPCExt6MEtlpSpec = Constraint(test_model.Time, rule=HPCExt6MEtlpSpec)
def HPCExt22MFracSpec(m, time, comp):
	return m.HPCExt22MFrac[time, comp] - m.HPCVapLvMFrac[time, 22, comp] == 0 
test_model.HPCExt22MFracSpec = Constraint(test_model.Time, test_model.Component, rule=HPCExt22MFracSpec)
def HPCExt22MEtlpSpec(m, time):
	return (m.HPCExt22MEtlp[time] - m.HPCVapLvMEtlp[time, 22])*  0.000010 == 0
test_model.HPCExt22MEtlpSpec = Constraint(test_model.Time, rule=HPCExt22MEtlpSpec)
#--------HPC Integration Initial Condition---------
def HPCICTrayMHldp(m):
	yield m.HPCTrayMHldp[0, 1] == 212.996919
	yield m.HPCTrayMHldp[0, 2] == 208.923963
	yield m.HPCTrayMHldp[0, 3] == 210.836299
	yield m.HPCTrayMHldp[0, 4] == 212.790966
	yield m.HPCTrayMHldp[0, 5] == 108.564402
	yield m.HPCTrayMHldp[0, 6] == 109.462276
	yield m.HPCTrayMHldp[0, 7] == 194.100893
	yield m.HPCTrayMHldp[0, 8] == 195.785052
	yield m.HPCTrayMHldp[0, 9] == 197.437998
	yield m.HPCTrayMHldp[0, 10] == 198.992435
	yield m.HPCTrayMHldp[0, 11] == 200.403976
	yield m.HPCTrayMHldp[0, 12] == 201.643837
	yield m.HPCTrayMHldp[0, 13] == 202.702672
	yield m.HPCTrayMHldp[0, 14] == 203.585383
	yield m.HPCTrayMHldp[0, 15] == 204.307240
	yield m.HPCTrayMHldp[0, 16] == 204.888123
	yield m.HPCTrayMHldp[0, 17] == 205.349945
	yield m.HPCTrayMHldp[0, 18] == 205.713638
	yield m.HPCTrayMHldp[0, 19] == 205.998056
	yield m.HPCTrayMHldp[0, 20] == 206.219293
	yield m.HPCTrayMHldp[0, 21] == 206.390934
	yield m.HPCTrayMHldp[0, 22] == 206.523693
	yield m.HPCTrayMHldp[0, 23] == 206.626314
	yield m.HPCTrayMHldp[0, 24] == 206.704047
	yield m.HPCTrayMHldp[0, 25] == 206.762796
	yield m.HPCTrayMHldp[0, 26] == 206.806943
	yield m.HPCTrayMHldp[0, 27] == 206.839818
	yield m.HPCTrayMHldp[0, 28] == 206.863953
	yield m.HPCTrayMHldp[0, 29] == 206.881256
	yield m.HPCTrayMHldp[0, 30] == 206.893189
	yield m.HPCTrayMHldp[0, 31] == 206.900759
	yield m.HPCTrayMHldp[0, 32] == 206.904842
	yield m.HPCTrayMHldp[0, 33] == 206.906043
	yield m.HPCTrayMHldp[0, 34] == 206.904752
	yield m.HPCTrayMHldp[0, 35] == 206.901478
	yield m.HPCTrayMHldp[0, 36] == 206.896356
	yield m.HPCTrayMHldp[0, 37] == 206.889686
	yield m.HPCTrayMHldp[0, 38] == 206.881552
	yield m.HPCTrayMHldp[0, 39] == 206.870550
	yield m.HPCTrayMHldp[0, 40] == 206.861775
	yield m.HPCTrayMHldp[0, 41] == 206.850353
	yield m.HPCTrayMHldp[0, 42] == 206.838259
test_model.HPCICTrayMHldp = ConstraintList(rule=HPCICTrayMHldp)
def HPCICTrayMCompHldp(m):
	yield m.HPCTrayMCompHldp[0, 1, "Nitrogen"] == 132.443645
	yield m.HPCTrayMCompHldp[0, 1, "Oxygen"] == 77.629664
	yield m.HPCTrayMCompHldp[0, 2, "Nitrogen"] == 136.438192
	yield m.HPCTrayMCompHldp[0, 2, "Oxygen"] == 69.625357
	yield m.HPCTrayMCompHldp[0, 3, "Nitrogen"] == 144.542974
	yield m.HPCTrayMCompHldp[0, 3, "Oxygen"] == 63.487637
	yield m.HPCTrayMCompHldp[0, 4, "Nitrogen"] == 152.738848
	yield m.HPCTrayMCompHldp[0, 4, "Oxygen"] == 57.375424
	yield m.HPCTrayMCompHldp[0, 5, "Nitrogen"] == 79.466819
	yield m.HPCTrayMCompHldp[0, 5, "Oxygen"] == 27.632182
	yield m.HPCTrayMCompHldp[0, 6, "Nitrogen"] == 83.049736
	yield m.HPCTrayMCompHldp[0, 6, "Oxygen"] == 24.762896
	yield m.HPCTrayMCompHldp[0, 7, "Nitrogen"] == 152.641478
	yield m.HPCTrayMCompHldp[0, 7, "Oxygen"] == 38.250571
	yield m.HPCTrayMCompHldp[0, 8, "Nitrogen"] == 159.362175
	yield m.HPCTrayMCompHldp[0, 8, "Oxygen"] == 32.937689
	yield m.HPCTrayMCompHldp[0, 9, "Nitrogen"] == 165.914920
	yield m.HPCTrayMCompHldp[0, 9, "Oxygen"] == 27.808172
	yield m.HPCTrayMCompHldp[0, 10, "Nitrogen"] == 172.062227
	yield m.HPCTrayMCompHldp[0, 10, "Oxygen"] == 23.042321
	yield m.HPCTrayMCompHldp[0, 11, "Nitrogen"] == 177.634408
	yield m.HPCTrayMCompHldp[0, 11, "Oxygen"] == 18.769567
	yield m.HPCTrayMCompHldp[0, 12, "Nitrogen"] == 182.532304
	yield m.HPCTrayMCompHldp[0, 12, "Oxygen"] == 15.058695
	yield m.HPCTrayMCompHldp[0, 13, "Nitrogen"] == 186.727636
	yield m.HPCTrayMCompHldp[0, 13, "Oxygen"] == 11.923766
	yield m.HPCTrayMCompHldp[0, 14, "Nitrogen"] == 190.245829
	yield m.HPCTrayMCompHldp[0, 14, "Oxygen"] == 9.336000
	yield m.HPCTrayMCompHldp[0, 15, "Nitrogen"] == 193.148613
	yield m.HPCTrayMCompHldp[0, 15, "Oxygen"] == 7.242176
	yield m.HPCTrayMCompHldp[0, 16, "Nitrogen"] == 195.514923
	yield m.HPCTrayMCompHldp[0, 16, "Oxygen"] == 5.574206
	yield m.HPCTrayMCompHldp[0, 17, "Nitrogen"] == 197.428870
	yield m.HPCTrayMCompHldp[0, 17, "Oxygen"] == 4.262161
	yield m.HPCTrayMCompHldp[0, 18, "Nitrogen"] == 198.970563
	yield m.HPCTrayMCompHldp[0, 18, "Oxygen"] == 3.240623
	yield m.HPCTrayMCompHldp[0, 19, "Nitrogen"] == 200.211598
	yield m.HPCTrayMCompHldp[0, 19, "Oxygen"] == 2.451778
	yield m.HPCTrayMCompHldp[0, 20, "Nitrogen"] == 201.213010
	yield m.HPCTrayMCompHldp[0, 20, "Oxygen"] == 1.846529
	yield m.HPCTrayMCompHldp[0, 21, "Nitrogen"] == 202.025709
	yield m.HPCTrayMCompHldp[0, 21, "Oxygen"] == 1.384516
	yield m.HPCTrayMCompHldp[0, 22, "Nitrogen"] == 202.690360
	yield m.HPCTrayMCompHldp[0, 22, "Oxygen"] == 1.033245
	yield m.HPCTrayMCompHldp[0, 23, "Nitrogen"] == 203.239640
	yield m.HPCTrayMCompHldp[0, 23, "Oxygen"] == 0.767093
	yield m.HPCTrayMCompHldp[0, 24, "Nitrogen"] == 203.692756
	yield m.HPCTrayMCompHldp[0, 24, "Oxygen"] == 0.568548
	yield m.HPCTrayMCompHldp[0, 25, "Nitrogen"] == 204.071579
	yield m.HPCTrayMCompHldp[0, 25, "Oxygen"] == 0.420735
	yield m.HPCTrayMCompHldp[0, 26, "Nitrogen"] == 204.392679
	yield m.HPCTrayMCompHldp[0, 26, "Oxygen"] == 0.310919
	yield m.HPCTrayMCompHldp[0, 27, "Nitrogen"] == 204.668680
	yield m.HPCTrayMCompHldp[0, 27, "Oxygen"] == 0.229458
	yield m.HPCTrayMCompHldp[0, 28, "Nitrogen"] == 204.909121
	yield m.HPCTrayMCompHldp[0, 28, "Oxygen"] == 0.169108
	yield m.HPCTrayMCompHldp[0, 29, "Nitrogen"] == 205.121279
	yield m.HPCTrayMCompHldp[0, 29, "Oxygen"] == 0.124456
	yield m.HPCTrayMCompHldp[0, 30, "Nitrogen"] == 205.310581
	yield m.HPCTrayMCompHldp[0, 30, "Oxygen"] == 0.091400
	yield m.HPCTrayMCompHldp[0, 31, "Nitrogen"] == 205.481118
	yield m.HPCTrayMCompHldp[0, 31, "Oxygen"] == 0.067014
	yield m.HPCTrayMCompHldp[0, 32, "Nitrogen"] == 205.636083
	yield m.HPCTrayMCompHldp[0, 32, "Oxygen"] == 0.048981
	yield m.HPCTrayMCompHldp[0, 33, "Nitrogen"] == 205.777851
	yield m.HPCTrayMCompHldp[0, 33, "Oxygen"] == 0.035692
	yield m.HPCTrayMCompHldp[0, 34, "Nitrogen"] == 205.908171
	yield m.HPCTrayMCompHldp[0, 34, "Oxygen"] == 0.025932
	yield m.HPCTrayMCompHldp[0, 35, "Nitrogen"] == 206.028610
	yield m.HPCTrayMCompHldp[0, 35, "Oxygen"] == 0.018736
	yield m.HPCTrayMCompHldp[0, 36, "Nitrogen"] == 206.140143
	yield m.HPCTrayMCompHldp[0, 36, "Oxygen"] == 0.013456
	yield m.HPCTrayMCompHldp[0, 37, "Nitrogen"] == 206.243694
	yield m.HPCTrayMCompHldp[0, 37, "Oxygen"] == 0.009561
	yield m.HPCTrayMCompHldp[0, 38, "Nitrogen"] == 206.339870
	yield m.HPCTrayMCompHldp[0, 38, "Oxygen"] == 0.006680
	yield m.HPCTrayMCompHldp[0, 39, "Nitrogen"] == 206.428995
	yield m.HPCTrayMCompHldp[0, 39, "Oxygen"] == 0.004584
	yield m.HPCTrayMCompHldp[0, 40, "Nitrogen"] == 206.514929
	yield m.HPCTrayMCompHldp[0, 40, "Oxygen"] == 0.003022
	yield m.HPCTrayMCompHldp[0, 41, "Nitrogen"] == 206.593090
	yield m.HPCTrayMCompHldp[0, 41, "Oxygen"] == 0.001890
	yield m.HPCTrayMCompHldp[0, 42, "Nitrogen"] == 206.665802
	yield m.HPCTrayMCompHldp[0, 42, "Oxygen"] == 0.001036
test_model.HPCICTrayMCompHldp = ConstraintList(rule=HPCICTrayMCompHldp)
def HPCICDtTrayMHldp(m, tray):
	if tray == 1:
		return (m.HPCLiqLvMFlow[0, tray + 1]- m.HPCLiqLvMFlow[0, tray] - m.HPCVapLvMFlow[0, tray]+m.HPCFeed1MFlow[0]-m.HPCDtTrayMHldp[0,tray])*0.001000 == 0
	elif tray == 4:
		return (m.HPCLiqLvMFlow[0, tray + 1] + m.HPCVapLvMFlow[0, tray - 1] - m.HPCLiqLvMFlow[0, tray] - m.HPCVapLvMFlow[0, tray]+m.HPCFeed2MFlow[0]-m.HPCDtTrayMHldp[0,tray])*0.001000 == 0
	elif tray == 6:
		return (m.HPCLiqLvMFlow[0, tray + 1] + m.HPCVapLvMFlow[0, tray - 1] - m.HPCLiqLvMFlow[0, tray] - m.HPCVapLvMFlow[0, tray]-m.HPCExt6MFlow[0]-m.HPCDtTrayMHldp[0,tray])*0.001000 == 0
	elif tray == 22:
		return (m.HPCLiqLvMFlow[0, tray + 1] + m.HPCVapLvMFlow[0, tray - 1] - m.HPCLiqLvMFlow[0, tray] - m.HPCVapLvMFlow[0, tray]-m.HPCExt22MFlow[0]-m.HPCDtTrayMHldp[0,tray])*0.001000 == 0
	elif tray == 42:
		return (m.HPCCondRefMFlow[0] + m.HPCVapLvMFlow[0, tray - 1] - m.HPCLiqLvMFlow[0, tray] - m.HPCVapLvMFlow[0, tray]-m.HPCDtTrayMHldp[0,tray])*0.001000 == 0
	else:
		return (m.HPCLiqLvMFlow[0, tray + 1] + m.HPCVapLvMFlow[0, tray - 1] - m.HPCLiqLvMFlow[0, tray] - m.HPCVapLvMFlow[0, tray]-m.HPCDtTrayMHldp[0,tray])*0.001000 == 0
test_model.HPCICDtTrayMHldp = Constraint(test_model.HPCTrays, rule=HPCICDtTrayMHldp)
def HPCICDtTrayPressure(m):
	yield m.HPCDtTrayPressure[0,1] == 0
	yield m.HPCDtTrayPressure[0,2] == 0
	yield m.HPCDtTrayPressure[0,3] == 0
	yield m.HPCDtTrayPressure[0,4] == 0
	yield m.HPCDtTrayPressure[0,5] == 0
	yield m.HPCDtTrayPressure[0,6] == 0
	yield m.HPCDtTrayPressure[0,7] == 0
	yield m.HPCDtTrayPressure[0,8] == 0
	yield m.HPCDtTrayPressure[0,9] == 0
	yield m.HPCDtTrayPressure[0,10] == 0
	yield m.HPCDtTrayPressure[0,11] == 0
	yield m.HPCDtTrayPressure[0,12] == 0
	yield m.HPCDtTrayPressure[0,13] == 0
	yield m.HPCDtTrayPressure[0,14] == 0
	yield m.HPCDtTrayPressure[0,15] == 0
	yield m.HPCDtTrayPressure[0,16] == 0
	yield m.HPCDtTrayPressure[0,17] == 0
	yield m.HPCDtTrayPressure[0,18] == 0
	yield m.HPCDtTrayPressure[0,19] == 0
	yield m.HPCDtTrayPressure[0,20] == 0
	yield m.HPCDtTrayPressure[0,21] == 0
	yield m.HPCDtTrayPressure[0,22] == 0
	yield m.HPCDtTrayPressure[0,23] == 0
	yield m.HPCDtTrayPressure[0,24] == 0
	yield m.HPCDtTrayPressure[0,25] == 0
	yield m.HPCDtTrayPressure[0,26] == 0
	yield m.HPCDtTrayPressure[0,27] == 0
	yield m.HPCDtTrayPressure[0,28] == 0
	yield m.HPCDtTrayPressure[0,29] == 0
	yield m.HPCDtTrayPressure[0,30] == 0
	yield m.HPCDtTrayPressure[0,31] == 0
	yield m.HPCDtTrayPressure[0,32] == 0
	yield m.HPCDtTrayPressure[0,33] == 0
	yield m.HPCDtTrayPressure[0,34] == 0
	yield m.HPCDtTrayPressure[0,35] == 0
	yield m.HPCDtTrayPressure[0,36] == 0
	yield m.HPCDtTrayPressure[0,37] == 0
	yield m.HPCDtTrayPressure[0,38] == 0
	yield m.HPCDtTrayPressure[0,39] == 0
	yield m.HPCDtTrayPressure[0,40] == 0
	yield m.HPCDtTrayPressure[0,41] == 0
	yield m.HPCDtTrayPressure[0,42] == 0
test_model.HPCICDtTrayPressure = ConstraintList(rule=HPCICDtTrayPressure)

#----------------------------------
#           HPCSump
#----------------------------------
#--------HPCSump Mass Balance---------
def HPCSumpMCompHldpSpec(m, time, comp):
	return (m.HPCSumpMCompHldp[time,comp] - m.HPCSumpHldpMFrac[time, comp] * m.HPCSumpMHldp[time])*0.001000 == 0
test_model.HPCSumpMCompHldpSpec = Constraint(test_model.Time, test_model.Component, rule=HPCSumpMCompHldpSpec)
def HPCSumpMassBlnc(m, time, comp):
	return (m.HPCSumpDtMCompHldp[time, comp]-m.HPCLiqLvMFlow[time,1]*m.HPCLiqLvMFrac[time,1, comp]+m.HPCSumpOutMFlow[time]*m.HPCSumpHldpMFrac[time, comp])*0.001000==0
test_model.HPCSumpMassBlnc = Constraint(test_model.Time,test_model.Component, rule=HPCSumpMassBlnc)
#--------HPCSump Summation---------
def HPCSumpLiqSum(m, time):
	return sum([m.HPCSumpHldpMFrac[time, c] for c in m.Component]) == 1
test_model.HPCSumpLiqSum = Constraint(test_model.Time, rule=HPCSumpLiqSum)
#--------HPCSump Holdup Level---------
def HPCSumpLevelCal(m, time):
	return m.HPCSumpHldpLevel[time] - m.HPCSumpMHldp[time] / m.HPCSumpLiqRho[time] / m.HPCSumpSumpCSArea == 0
test_model.HPCSumpLevelCal = Constraint(test_model.Time, rule=HPCSumpLevelCal)
#--------HPCSump Integration Initial Condition---------
def HPCSumpICMHldp(m):
	return m.HPCSumpMHldp[0] == m.HPCSumpLevelSP[0]*m.HPCSumpSumpCSArea                                *m.HPCSumpLiqRho[0]
test_model.HPCSumpICMHldp = Constraint(rule=HPCSumpICMHldp)
def HPCSumpICCompHldp(m):
	yield m.HPCSumpMCompHldp[0,"Nitrogen"] == m.HPCSumpLevelSP[0]*m.HPCSumpSumpCSArea                                *m.HPCSumpLiqRho[0]*0.621810
	yield m.HPCSumpMCompHldp[0,"Oxygen"] == m.HPCSumpLevelSP[0]*m.HPCSumpSumpCSArea                                *m.HPCSumpLiqRho[0]*0.364464
test_model.HPCSumpICCompHldp = ConstraintList(rule=HPCSumpICCompHldp)
#--------HPCSump Level Control---------
def HPCSumpLCDefError(m, time):
	return m.HPCSumpLCError[time] - m.HPCSumpHldpLevel[time] + m.HPCSumpLCParaCVSS == 0
test_model.HPCSumpLCDefError = Constraint(test_model.Time,rule=HPCSumpLCDefError)
def HPCSumpLCPILaw(m, time):
	return m.HPCSumpLCParaMVSS + m.HPCSumpLCParaKc * (m.HPCSumpHldpLevel[time] - m.HPCSumpLCParaCVSS)+m.HPCSumpLCParaKc/m.HPCSumpLCParaTi*m.HPCSumpLCSumError[time]-m.HPCSumpOutMFlow[time] == 0
test_model.HPCSumpLCPILaw = Constraint(test_model.Time,rule=HPCSumpLCPILaw)
def HPCSumpLCICSumError(m):
	return m.HPCSumpLCSumError[0] == 0
test_model.HPCSumpLCICSumError = Constraint(rule=HPCSumpLCICSumError)

#----------------------------------
#           HPCCond
#----------------------------------
#--------HPCCond Mass Balance---------
def HPCCondMassBlnc(m,time):
	return (m.HPCCondRefMFlow[time]+m.HPCCondPrdtMFlow[time]-m.HPCVapLvMFlow[time,42])*0.001000==0
test_model.HPCCondMassBlnc = Constraint(test_model.Time, rule=HPCCondMassBlnc)
def HPCCondRefSpec(m,time):
	return (m.HPCCondRefMFlow[time]-m.HPCVapLvMFlow[time,42]*m.HPCCondRefluxRatio[time])*0.001000==0
test_model.HPCCondRefSpec = Constraint(test_model.Time, rule=HPCCondRefSpec)
#--------HPCCond Energy Balance---------
def HPCCondEngBlnc(m,time):
	return (m.HPCVapLvMFlow[time,42]*(m.HPCVapLvMEtlp[time,42]-m.HPCCondOutMEtlp[time])-m.HPCCondMHeatOut[time])*0.000010==0
test_model.HPCCondEngBlnc = Constraint(test_model.Time, rule=HPCCondEngBlnc)
#--------HPCCond Bubble Point---------
def HPCCondSelfBubTemp(m,time):
	return m.HPCVapLvMFrac[time,42,"Oxygen"] == triHPCThermo.HPCCondSelfCstmLiqO2.LiqO2(m.HPCTrayPressure[time,42],m.HPCCondTemp[time],m.HPCVapLvMFrac[time,42,"Nitrogen"])
test_model.HPCCondSelfBubTemp = Constraint(test_model.Time,rule=HPCCondSelfBubTemp)

#===================================
#
#         Discretize
#
#===================================
Discretizer.discretilize(test_model)

#===================================
#
#     Variable Initialization
#
#===================================
ModularTask.InitValueTools.load_naive_var_init(test_model,"test_modelNaiveInit.txt")	