## Introduction

In this mini project you will be working with a dataset about the road accidents in Los Angeles. The data you will be working with is a subset of data present [here](https://www.kaggle.com/datasets/cityofLA/los-angeles-traffic-collision-data)


### Data Description

The data shared with you [here](./data/) contains the following files:

1. `incidents.csv`: This is the main file, each row is a unique incident.
2. `area.csv`: This contains information on localities, join this with incidents file.
3. `victims.csv`: This contains data on fatalities in each incident, this can also be joined with incidents file.
4. `latlong.json`: This contains data on latitude and longitude of each incident. This can also be joined with the incidents file, if needed.

### Tasks:

You need to complete the code given in the `src` directory.

**Task 1**:

Refer to the [file](./src/get_incident_details.py) and complete the following methods of the class `Incidents`

1. `analyze_area`
2. `analyze_area_drilldown`
3. `plot_num_incidents_all`
4. `find_avg_age_victim`

Verify if the class works by running the tests in `tests/test_incident.py`
Use the following command to run the tests:

```shell
python -m unittest tests/test_incident.py
```