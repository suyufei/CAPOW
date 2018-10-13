# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 16:20:03 2018

@author: sdenaro
"""
import sys
import Willamette_model as inner #reading in the inner function
#import time
initial_doy=1 #Set the simulation initial_doy
sys.argv = ["PNW_hydro/Willamette/settings.xml", str(initial_doy)] #simulation inputs
#starttime = time.time()
execfile("PNW_hydro/Willamette/Willamette_outer.py")
#elapsed = time.time() - starttime