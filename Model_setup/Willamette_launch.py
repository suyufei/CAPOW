# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 16:20:03 2018

@author: sdenaro
"""
import sys
sys.path.append('../Stochastic_engine/PNW_hydro/Willamette/')
import Willamette_model as inner #reading in the inner function
#import time
initial_doy=1 #Set the simulation initial_doy
sys.argv = ["../Stochastic_engine/PNW_hydro/Willamette/settings.xml", str(initial_doy)] #simulation inputs
#starttime = time.time()
execfile("../Stochastic_engine/PNW_hydro/Willamette/Willamette_outer.py")
#elapsed = time.time() - starttime