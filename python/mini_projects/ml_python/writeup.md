## Introduction

In this mini project you will be working with a dataset about the road accidents in Los Angeles. The data you will be working with is a subset of data present [here](https://www.kaggle.com/datasets/cityofLA/los-angeles-traffic-collision-data)

The aim of this project is to develop a cli application that can be used to query different aspects of this dataset. You are working in a team that consist of data scientists, data analysts and ml engineers. In this project you will be building tools that can be used to team of data scientists and data analysts. Your prime responsibility is to build a python application that can help the team generate meaningful data visualizations and do common queries on the data.

Your application will be a command line app. You will be using the skills you've learn't so far, such as python programming, object oriented programming, working with pandas and numpy as well as creating commandline applications and using unittests.

### Data Description

The data shared with you [here](./data/) contains the following files:

1. `incidents.csv`: This is the main file, each row is a unique incident.
2. `area.csv`: This contains information on localities, join this with incidents file.
3. `victims.csv`: This contains data on fatalities in each incident, this can also be joined with incidents file.
4. `latlong.json`: This contains data on latitude and longitude of each incident. This can also be joined with the incidents file, if needed.


### Tasks:

You need to complete the code given in the `src` directory.


**Task 1**

Refer to the [file](./src/dq.py) and complete the following methods of the class `DataQuality`

1. `_create_dq_numeric_vars`
2. `_create_dq_categorical_var`
3. `create_dq`

Verify if the class works by running the tests in `tests/test_dq.py`
Use the following command to run the tests:

```shell
python -m unittest tests/test_dq.py
```

**Task 2**:

Refer to the [file](./src/incidents.py) and complete the following methods of the class `Incidents`

1. `num_incidents_area`
2. `plot_num_incidents_all`
3. `find_incidents_area_date_range`
4. `plot_heatmap_areas`

Verify if the class works by running the tests in `tests/test_incident.py`
Use the following command to run the tests:

```shell
python -m unittest tests/test_incident.py
```

**Task 3**
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

**Task4**

Refer to the [file](./src/locations.py) and complete the following methods in `Location` class

1. `compute_avg_distance`
2. `plot_avg_distance_areas`

Verify if the class works by running the tests in `tests/test_locations.py`
Use the following command to run the tests:

```shell
python -m unittest tests/test_locations.py
```
**Task 5**

Refer to the file `main.py`. This is the final file which will bring together all the classes created in the previous tasks. You
will need to generate the cli app in this file by completing the 
following functions:

1. `generate_dq_report`
2. `find_incidents`
3. `create_plot_incidents`
4. `incidents_area_date_range`
5. `plot_heatmapAreas`
6. `find_avg_age`
7. `plot_avgAge`
8. `plot_distAge`
9. `plot_yearArea`
10. `compute_avgDist`
11. `plot_avgDist`

Also add logging at appropriate places.

<todo> Description of commands and the functions they will perform

### Rubric
<todo>

### Sample Readme Format
<todo>

###
**Submission Guidelines**

Push your code to a github repository. Write an informative Readme file and submit to us the github link.

<todo> Modifications