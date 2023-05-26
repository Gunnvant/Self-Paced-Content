import pandas as pd
import matplotlib as plt
import seaborn as sns
from __future__ import annotations

class Incidents():
    def __init__(self,path_incidents,path_area):
        self.path_incidents = path_incidents
        self.path_area = path_area

    def num_incidents_area(self,start_date:str|None,end_date:str|None)->dict:
        '''
        This should return a dict of the following form:
        {'area_name':num_incidents,'area_name':num_incidents}
        If the start_date and end_date is None then the dict for the
        while time range should be returned. The date is in dd/mm/yyyy format
        In case either of them is None then a meaningful exception
        should be raised. Ref: https://www.w3schools.com/python/ref_keyword_raise.asp
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
