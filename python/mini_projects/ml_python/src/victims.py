import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from __future__ import annotations

class Victims():
    def __init__(self,path_incidents,path_victims,path_area):
        self.path_incidents = path_incidents
        self.path_victims = path_victims
        self.path_area = path_area
    
    def get_avg_age(self,area:str|None)->float:
        '''
        Find average age of victims for a given area. 
        In case area is none, find average age for all
        areas
        '''
        pass

    def plot_avg_age_areas(self,areas:list):
        '''
        Given a list of areas, plot the average age and save
        the plot in ./plots/avg_age_areas.png
        '''
        pass

    def plot_dist_age_years(self,years:list|None):
        '''
        Create an appropriate plot to show distribution of age
        of victims, year on year. Save in ./plots/dist_age_victims.png
        In case years is None, then make the plot for all the years.
        '''
        pass

    def plot_year_area(sef,years:list|None,areas:list|None):
        '''
        Create a heatmap of avg age of victims across
        areas and years. Save in ./plots/heatmap_avg_age.png
        In case the years is None then make the plot for all the years
        In case the areas is None then make the plot for all the areas
        '''
        pass

