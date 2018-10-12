# Creation of stochastic inputs
The primary engine that drives CAPOW system dynamics is the stochastic modeling of meteorological (temperatures, wind speeds) and hydrologic (streamflow) variables at sites distributed throughout the West Coast, including 17 NOAA NCDC monitoring stations, and approximately 60 stream gauges. A range of stochastic modeling approaches is used to re-produce statistical moments, and spatial and temporal statistical structures. 

These synthetic weather and streamflow data are then pushed through a suite of models that convert them to relevant power system inputs (hourly electricity demand, hourly solar power production, hourly wind power production, daily hydropower availability, and daily power flows between the core UC/ED zones and other zones in the WECC footprint).

## stochastic_engine.py
This is the primary file that executes every other script. At the top of the file is a section that performs a statistical analysis of historical meterological data. This only needs to be executed a single time, the first time CAPOW is used. The resultant data files are included as part of the CAPOW package, so the default is for this script to be commented out. 

Near the top of the file, the user must specify a certain number of years worth of stochastic inputs to create. Note that regardless of the number selected, the CAPOW default is to push only a single synthetic year through the UC/ED model.

<img src="https://github.com/romulus97/CAPOW/blob/master/Wiki_images/readme1.png" alt="alt text" width="640" height="480">
