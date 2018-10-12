# Creation of stochastic inputs
The primary engine that drives CAPOW system dynamics is the stochastic modeling of meteorological (temperatures, wind speeds) and hydrologic (streamflow) variables at sites distributed throughout the West Coast, including 17 NOAA NCDC monitoring stations, and approximately 60 stream gauges. A range of stochastic modeling approaches is used to re-produce statistical moments, and spatial and temporal statistical structures. 

These synthetic weather and streamflow data are then pushed through a suite of models that convert them to relevant power system inputs (hourly electricity demand, hourly solar power production, hourly wind power production, daily hydropower availability, and daily power flows between the core UC/ED zones and other zones in the WECC footprint).

## stochastic_engine.py
This is the primary file that executes every other stochastic modeling script. At the top of the file is a section that performs a statistical analysis of historical meterological data. This only needs to be executed a single time, the first time CAPOW is used. The resultant data files are included as part of the CAPOW package, so the default is for this script to be commented out. 

Near the top of the file, the user must specify a certain number of years worth of stochastic inputs to create (**sim_years = X**). Note that regardless of the number selected, the CAPOW default is to push only a single synthetic year through the UC/ED model.

<img src="https://github.com/romulus97/CAPOW/blob/master/Images/readme1.png" alt="alt text" width="500" height="300">

Immediately below, stochastic_engine passes the user specified number of stochastic years to the synthetic_temps_wind file and its function synthetic_temps_wind.sythetic().

## synthetic_temps_wind.py
This file takes its inputs from the statistical analysis of historical meteorological data (daily average profiles of wind and temperature, records of deviations (residuals) from those profiles, and a covariance matrix of "whitended" (de-seasoned) residuals across all meteorological fields and locations. Using these data, it fits a vector autoregressive (VAR) model to whitened meteorological residuals, re-seasons them and adds that data to the daily average profiles to arrive at synthetic daily weather data at each station represented.

**Input files required:** <br/>
Historical_weather_analysis/WIND_TEMP_res.csv <br/>
Historical_weather_analysis/Covariance_Calculation.csv <br/>
Historical_weather_analysis/WIND_TEMP_ave.csv <br/>
Historical_weather_analysis/WIND_TEMP_std.csv <br/>

**Output files:** <br/>
Synthetic_Weather/synthetic_weather_data.csv

## synthetic_streamflows.py
This develops statistical relationships between total annual streamflow at each gauge site and total annual heating and cooling degree days. Whitened residuals from these regressions are used to calculate an associated covariance matrix. Total annual streamflows at each site are then simulated as the sum of predicted regression values and random samples from a multivariate normal defined by the historical covariance matrix. Daily flow fractions (the amount of streamflow experienced as a fraction of the annual total) are then conditionally re-sampled from the historical record using summer temperatures. 

**Input files required:** <br/>
Synthetic_streamflows/hist_temps_1953_2007.xlsx <br/>
Synthetic_streamflows/BPA_hist_streamflow.xlsx <br/>
Synthetic_streamflows/Hoover_hist_streamflow.csv <br/>
Synthetic_streamflows/CA_hist_streamflow.xlsx <br/>
Synthetic_streamflows/Willamette_hist_streamflow.csv <br/>
Synthetic_streamflows/city_weights.xlsx <br/>
Synthetic_weather/synthetic_weather_data.csv <br/>

**Output files:** <br/>
Synthetic_streamflows/synthetic_streamflows_FCRPS.csv <br/>
Synthetic_streamflows/synthetic_streamflows_TDA.csv <br/>
Synthetic_streamflows/synthetic_discharge_Hoover.csv <br/>
Synthetic_streamflows/synthetic_streamflows_CA.csv <br/>
Synthetic_streamflows/synthetic_streamflows_Willamette.csv <br/>

<img src="https://github.com/romulus97/CAPOW/blob/master/Images/readme2.png" alt="alt text" width="570" height="280">

## CA_hydropower.py
This file predicts aggregated daily hydropower production for two zones in the CAISO system (PG&E Valley and Southern California Edison). The primary inputs to this simulation are synthetic streamflows. No mass balance hydrologic models are available for most dams in these zones, so simple rule based prediction models were parameterized via a differential evolution algorithm. 

**Input files required:** <br/>
CA_hydropower/sites.xlsx <br/>
CA_hydropower/upper.xlsx <br/>
CA_hydropower/calender.xlsx <br/>
CA_hydropower/hist_reservoir_inflows.xlsx <br/>
CA_hydropower/PGE_DE_V1
CA_hydropower/SCE_DE_V1
CA_hydropower/A1.0_FNF_Storage_Rule_Belden
CA_hydropower/A1.0_FNF_Storage_Rule_Butt_Valley
CA_hydropower/A1.0_FNF_Storage_Rule_Caribou_1
CA_hydropower/A1.0_FNF_Storage_Rule_Caribou_2
Synthetic_streamflows/synthetic_streamflows_CA.csv <br/>

**Output files:** <br/>
Synthetic_streamflows/synthetic_streamflows_FCRPS.csv <br/>
Synthetic_streamflows/synthetic_streamflows_TDA.csv <br/>
Synthetic_streamflows/synthetic_discharge_Hoover.csv <br/>
Synthetic_streamflows/synthetic_streamflows_CA.csv <br/>
Synthetic_streamflows/synthetic_streamflows_Willamette.csv <br/>
