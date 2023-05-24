import pandas as pd
import matplotlib as plt
import seaborn as sns
from __future__ import annotations

class Incidents():
    def __init__(self,path_incidents,path_area,path_victims,path_latlong):
        self.path_incidents = path_incidents
        self.path_area = path_area
        self.path_victims = path_victims
        self.path_latlong = path_latlong

    def analyze_area(self)->dict:
        '''
        This should return a dict of the following form:
        {'area_name':num_incidents,'area_name':num_incidents}
        '''
        pass
    def analyze_area_drilldown(self,month:int,year:int)->dict:
        '''
        This will take year as an input and will return the dict 
        of the following form
        {'area_name':num_incidents,'area_name':num_incidents}
        for a given month and year.
        '''
        pass
    def plot_num_incidents_all(self):
        '''
        This should create and save a plot named './plots/trend_incidents.png'
        that will show how the total number of incidents have trended over
        time.
        '''
        pass

    def find_avg_age_victim(self,area:str|None,gender:str|None)->float:
        '''
        This will compute average age of victims for a given area 
        and gender. If both area and gender are None then it should 
        return average of the whole data. If only area is None then 
        for the average of given gender and all areas. If only gender
        is None then for the given area and all the genders.
        '''
        pass
