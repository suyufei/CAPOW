# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 22:17:00 2018

@author: jkern
"""

from __future__ import division
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

########################################################
# This script calculates daily hydropower production for 
# PNW zone using FCRPS, Willamette, and missing dams. 

# FCRPS
df_FCRPS = pd.read_csv('PNW_hydro/FCRPS/Modeled_BPA_Dams.csv',header=None)
FCRPS = df_FCRPS.values
F = np.sum(FCRPS,axis=1)

# Willamette
#df_Willamette = pd.read_excel('PNW_hydro/Willamette/Output/Willamette_simulation_hydropower.xlsx')
#W=df_Willamette.values

# Missing Dams


df_total = pd.DataFrame(F) 
df_total.columns = ['PNW']
df_total.to_excel('PNW_hydro/PNW_hydro_daily.xlsx')

 