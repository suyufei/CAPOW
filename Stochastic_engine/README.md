# Creation of stochastic inputs
The primary engine that drives CAPOW system dynamics is the stochastic modeling of meteorological (temperatures, wind speeds) and hydrologic (streamflow) variables at sites distributed throughout the West Coast, including 17 NOAA NCDC monitoring stations, and approximately 60 stream gauges. A range of stochastic modeling approaches is used to re-produce statistical moments, and spatial and temporal statistical structures. 

These synthetic weather and streamflow data are then pushed through a suite of models that convert them to relevant power system inputs (hourly electricity demand, hourly solar power production, hourly wind power production, daily hydropower availability, and daily power flows between the core UC/ED zones and other zones in the WECC footprint).

## stochastic_engine.py
The primary file 
