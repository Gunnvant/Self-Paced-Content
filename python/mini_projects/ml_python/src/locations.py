import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from __future__ import annotations

class Location():
    def __init__(self,path_incidents,path_latlong,path_area):
        self.path_incidents = path_incidents
        self.path_latlong = path_latlong
        self.path_area = path_area

    def compute_avg_distance(self,area:str,incident_date:str|None)->float:
        '''
        Should compute average distance between incidents (in km)
        Use the haversine formula to compute distance between
        points when latitude and longitude is known. 
        Ref:https://stackoverflow.com/questions/4913349/haversine-formula-in-python-bearing-and-distance-between-two-gps-points
        You can compute the distance between all the pairs of the points and find their
        average. For example if there are three points, then average will be
        D(A,B)+D(A,C)+D(B,C)/3. D(a,b)->Distance between points a and b
        
        Args
        area: Name of areas
        incident_date: date of incident (dd/mm/yyyy), if None then for the whole time period

        '''
        pass
    def plot_avg_distance_areas(self,year:str):
        '''
        Plot the avg distance between incidents for a given year across all the 
        areas. Plot to be saved in ./plots/avg_distance_{area_name}.png
        Year should be in yyyy format
        '''
        pass