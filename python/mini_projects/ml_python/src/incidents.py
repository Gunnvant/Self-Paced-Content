import pandas as pd
import matplotlib as plt
import seaborn as sns
from __future__ import annotations

class Incidents():
    def __init__(self,path_incidents,path_area):
        self.path_incidents = path_incidents
        self.path_area = path_area

    def analyze_area(self)->dict:
        '''
        This should return a dict of the following form:
        {'area_name':num_incidents,'area_name':num_incidents}
        '''
        pass
    def analyze_area_drilldown(self,month:int,year:int)->dict:
        '''
        This will take year and month as an input and will return the dict 
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

    def find_incidents_area_date_range(self,area:str|None,start_date:str|None,end_date:str|None)->int:
        '''
        This will compute the number of incidents in a given area for a date range
        If area is None, then find number of incidents for all areas in a given date range.
        If start_date and end_date is None, the find the number of incidents in an area for
        the complete duration.
        If area, start_date and end_date is None then find the total number of incidents
        '''
        pass

    def plot_heatmap_areas(self,years:list|None,areas:list|None):
        '''
        This will create a heatmap of number of incidents by area and year
        Save the plot in ./plots/heatmap_num_area.png
        In case the years is None then make the plot for all the years
        In case the areas is None then make the plot for all the areas
        '''
        pass
