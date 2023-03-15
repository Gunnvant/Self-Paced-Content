## Python Case Study

**Task 1**
You have been given a dump of data from UK's crime listing. The dataset is [here](https://drive.google.com/file/d/1vJ9uU5QmmhBRttCd-2IZXu7fefJD0R99/view?usp=sharing). 

The dataset contains data pertaining to three main categories:
1. Street crimes
2. Crime outcomes
3. Stop and Search events on a highway

In the current form, the data is distributed across different csv files. For each neighborhood, there are atmost three variants, one corresponding to street crimes, one corresponding to crime outcomes and one corresponding to stop and search events.

Your task is to concatenate all the data corresponding to each category in a single file. 

At the end of this exercise you will have generated three files. One corresponding to each of the three main categories mentioned above.

In order to accomplish this task you can use the following rules:
1. Any filename that has the phrase `street.csv`, pertains to the category `Street Crimes`
2. Any filename that has the phrase `outcomes.csv`, pertains to the category `Crime Outcomes`
3. Any filename that has the phrase `stop-and-search.csv`, pertains to the category `Stop and Search`

**Task 2**
You have been tasked with generating a csv file out of a json datatset. The location of the dataset is [here](https://data.montgomerycountymd.gov/api/views/v76h-r7br/rows.json?accessType=DOWNLOAD)

The first thing you need to do is generate the data-dictionary from this json file. This file has a field named `meta`, embedded in this field is the detail on each column. You need to create a csv file which contains the following fields:
1. Name of the column
2. Description of the column (if available)
3. Datatype

After you have generated the data dictionary you need to put the relevant data into a tabular form (csv or a tsv file). You must keep in mind the data types while putting the data in a table. If a field is a numeric field you need to make sure that while creating a csv or a tsv file the data-type is taken care of.


**Task 3**

Use the `peter_pan.txt`. Download the file [here](https://drive.google.com/file/d/1D4q06bZ_hSEICxE8j843N4KasLq8YWPq/view?usp=sharing)  to answer the questions. 

a. The number of characters in the file are?

1. 274394
2. 274951
3. 374950
4. 374951

Provide your code here
```python
your code goes here
```

b. How many chapters does this text have?

1. 18
2. 17
3. 16
4. 21

Provide your code here
```python
your code goes here
```

c. Find the index where Chapter II starts?

Provide your code here
```python
your code goes here
```

d. Find the index where Chapter III starts?

Provide your code here
```python
your code goes here
```

e. How many characters/alphabets/symbols (including white spaces etc) are there in Chapter II?

1. 15926
2. 15921
3. 15929
4. 15920

Provide your code here
```python
your code goes here
```

**Task 4**

a. Use the dataset called [narcos.json](https://drive.google.com/file/d/1JdRVciBHaPu33Gc461nk6Y28EBD8dfyL/view?usp=sharing). In this json file is there a key named `WebChannel`?

1. Yes
2. No

```python
your code goes here
```
b. Now define a function called `fetch()` which takes the dictionary created after reading the json file and returns a list of lists with following fields:

1. id of the episode
2. url of the episode
3. name of the episode
4. season of the episode
5. number of the episode
6. type
7. airdate
8. airtime
9. airtimestamp
10. runtime
11. summary (Remove the ```<p>``` and ```</p>``` tags from the summary)

``` python
def fetch(dicttionary_json_data):
# your code goes here
    return result ##result should be a list of lists with the fields given above.

```

c. Now write a function named `dump()` which will write the contents of the results obtained from `fetch()` defined earlier to a csv file. The headers of the file should be in the following order:

1. id 
2. url 
3. name 
4. season 
5. number 
6. type
7. airdate
8. airtime
9. airtimestamp
10. runtime
11. summary 

The function should take the following inputs:
1. Path where you want to save the results
2. The name you want to give this file
3. The output of `fetch()` function

The function should return:
1. True if file has been created
2. False otherwise (Hint use the `os` module in python to check if a file at a given location exits or not)

```python
import os
import csv
def dump(path,name,results):
    '''Your code goes here'''
    
```
## How to submit?
For `task1`,`task2`,`task3` and `task4` you need to submit separate notebooks. Make your notebooks modular as we will change the paths in the notebooks submitted by you and run the codes again to test your submission.

We encourage you to use github to make this submission. Use the submission structure given below.We further, encourage you to write a good readme for the github repo. You can then show this as some of the projects you've done on github in your resume.

You can submit a text file with link to the github repository. You can view the self paced content on github to create and submit code to your repositories.

Below are some examples of good readme and github project structure:

- [Example Readme](https://github.com/Wittline/uber-expenses-tracking)
- [Example Readme](https://github.com/JarrodAJ/sec_employee_information_extraction)
- [Example Readme](https://github.com/Gunnvant/autocomplete_ngrams)
- [Example Readme](https://github.com/Gunnvant/calendar_parser)

You can follow the submission structure given [here]((./submission_structure/)) 


## Python Versions and Package Requirements

The python version and package requirements are [here](./env.yaml)
