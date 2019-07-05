naive_dynamic 没有加入微分方程，只是添加了一个t的索引，变成了准动态问题
no_index_reduction 加入了微分方程，使用的是线性水力学，没有进行index reduction，dmi/dt认为是dM/dt*xi
with_dmidt dmi/dt修正为d(M*xi)/dt，但能量守恒仍用的是dH/dt = dM/dt*h
with_dhdt dH/dt修正为d(M*h)/dt，这样就与index_reduction模型一致了
index_reduction模型对能量守恒进行了改写，使得index降为1
