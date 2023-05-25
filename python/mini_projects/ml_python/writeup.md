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

Refer to the [file](./src/incidents.py) and complete the following methods of the class `Incidents`

1. `analyze_area`
2. `analyze_area_drilldown`
3. `plot_num_incidents_all`
4. `find_incidents_area_date_range`
5. `plot_heatmap_areas`

Verify if the class works by running the tests in `tests/test_incident.py`
Use the following command to run the tests:

```shell
python -m unittest tests/test_incident.py
```

**Task 2**
Refer to the [file](src/victims.py) and complete the following methods for the class `Victims` 

1. `get_avg_age`
2. `plot_avg_age_areas`
3. `plot_dist_age_years`
4. `plot_year_area`

Verify if the class works by running the tests in `tests/test_victims.py`
Use the following command to run the tests:

```shell
python -m unittest tests/test_victims.py
```

**Task3**

Refer to the [file](./src/locations.py) and complete the following methods in `Location` class

1. `compute_avg_distance`
2. `plot_avg_distance_areas`

Verify if the class works by running the tests in `tests/test_locations.py`
Use the following command to run the tests:

```shell
python -m unittest tests/test_locations.py
```


**Submission Guidelines**

Push your code to a github repository. Write an informative Readme file and submit to us the github link.