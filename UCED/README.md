
## Model Simulation
The user specifies a number of days out of the randomly sampled synthetic year to simulated (**min = 2, max = 365**). Then the CAISO and PNW dispatch models are run in sequence.

<img src="https://github.com/romulus97/CAPOW/blob/master/Images/readme8.png" alt="alt text" width="500" height="400">

## CA_wrapper.py
This file iteratively loads power system inputs 48-hours at a time and dispatches the model over a 2-day operating horizon. Results (power flows, generation schedules) are dynamically stored for each simulation day (24-hour period).

**Input files required:** <br/>
..Model_setup/CA_data_file/data.dat 
CA_dispatch.py

**Output files:** <br/>
CAISO/flow.csv
CAISO/mwh_1.csv
CAISO/mwh_2.csv
CAISO/mwh_3.csv
CAISO/nrsv.csv
CAISO/on.csv
CAISO/solar_out.csv
CAISO/wind_out.csv
CAISO/switch.csv
CAISO/srsv.csv

## PNW_wrapper.py
This file iteratively loads power system inputs 48-hours at a time and dispatches the model over a 2-day operating horizon. Results (power flows, generation schedules) are dynamically stored for each simulation day (24-hour period).

**Input files required:** <br/>
..Model_setup/PNW_data_file/data.dat 
PNW_dispatch.py

**Output files:** <br/>
PNW/flow.csv
PNW/mwh_1.csv
PNW/mwh_2.csv
PNW/mwh_3.csv
PNW/nrsv.csv
PNW/on.csv
PNW/solar_out.csv
PNW/wind_out.csv
PNW/switch.csv
PNW/srsv.csv
