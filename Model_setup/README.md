# UC/ED Model setup
Once stochastic inputs are created, a single year is randomly sampled and that year's data is put in the .dat format that is required for the pyomo mathematical optimization library. This script can easily be interfaced with a data mining scheme for selecting specific years/scenarios to run on a cluster. 

<img src="https://github.com/romulus97/CAPOW/blob/master/Images/readme5.png" alt="alt text" width="500" height="300">

## min_hydro_ramping.py
This section uses historical hydropower production data and simulated hydropower to create time series of minimum hydropower production and "ramp rates" for dispatchable hydropower in each zone.

**Input files required:** <br/>
Hydro_setup/PNW_hydro_2001.xlsx <br/>
Hydro_setup/PNW_hydro_2005.xlsx <br/>
Hydro_setup/PNW_hydro_2010.xlsx <br/>
Hydro_setup/PNW_hydro_2011.xlsx <br/>
Hydro_setup/PGEV_hydro_2001.xlsx <br/>
Hydro_setup/PGEV_hydro_2005.xlsx <br/>
Hydro_setup/PGEV_hydro_2010.xlsx <br/>
Hydro_setup/PGEV_hydro_2011.xlsx <br/>
Hydro_setup/SCE_hydro_2001.xlsx <br/>
Hydro_setup/SCE_hydro_2005.xlsx <br/>
Hydro_setup/SCE_hydro_2010.xlsx <br/>
Hydro_setup/SCE_hydro_2011.xlsx <br/>

**Output files:** <br/>
Hydro_setup/Minimum_hydro.xlsx <br/>

<img src="https://github.com/romulus97/CAPOW/blob/master/Images/readme6.png" alt="alt text" width="530" height="300">
