#!/usr/bin/env python
#-*- coding:utf-8 -*-
from pyomo.environ import *
from pyomo.dae import *
model = ConcreteModel()
model.time = ContinuousSet(bounds=(0,10)) # Unscaled time
#---------------物质组分指定-----------
model.Component = Set(initialize=['Oxygen','Nitrogen'])
model.FeedMolarFraction = Param(model.time, model.Component, initialize={'Oxygen':0.21,'Nitrogen':0.79})
discretizer = TransformationFactory('dae.collocation')
discretizer.apply_to(model, nfe=5, scheme='LAGRANGE-RADAU')

print(model.FeedMolarFraction.value)