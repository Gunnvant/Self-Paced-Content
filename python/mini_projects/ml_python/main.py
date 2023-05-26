import pandas as pd
from src import dq,incidents,locations,victims
import argparse
import logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(message)s')

def generate_dq_report(path):
    '''
    Generate a data quality report and save the
    numeric and categorical report in the current
    working directory. The files should be saved with
    the following name {parent_file_name}_{cat/num}.csv
    Example: If the parent file is area.csv, then two
    files will be created: area_num.csv, area_cat.csv.
    '''
    dq = dq.DataQuality(path)
    ## your code
    pass

def find_incidents(incident_obj,start_date,end_date):
    '''
    Call the Incidents.num_incidents_area()
    '''
    ##your code
    pass
def create_plot_incidents(incident_obj):
    '''
    Call the Incidents.plot_num_incidents_all()
    '''
    ## your code
    pass

def incidents_area_date_range(incident_obj,area,start_date,end_date):
    '''
    Call the Incidents.find_incidents_area_date_range()
    '''
    ## your code
    pass

def plot_heatmapAreas(incident_obj,area_list,year_list):
    '''
    Call the Incidents.plot_heatmap_areas(area_list,year_list)
    '''
    ## your code
    pass

def find_avg_age(victim_obj,area):
    '''
    Call Victims.get_avg_age()
    '''
    ## your code
    pass

def plot_avgAge(victims_object,area):
    '''
    Call Victims.plot_avg_age_area()
    '''
    ## your code
    pass

def plot_distAge(victims_object,year_list):
    '''
    Call Victims.plot_dist_age_years()
    '''
    ## your code
    pass
def plot_yearArea(victims_object,year_list,area_list):
    '''
    Call Victims.plot_year_area()
    '''
    ## your code
    pass
def compute_avgDist(location_object,area,incident_date):
    '''
    Call Locations.compute_avg_distance()
    '''
    ## your code
    pass
def plot_avgDist(location_object,year):
    '''
    Call Locations.plot_avg_distance_areas()
    '''
    ## your code
    pass

parser = argparse.ArgumentParser(description='Main program to run cli app')
parser.add_argument("--path_csv_dq",
                    type=str,
                    required=False,help="Path to csv file whose data quality report needs to be generated")
parser.add_argument("--start_date",
                    type=str,
                    help="Start date for reporting in dd/mm/yyyy format")
parser.add_argument("--end_date",
                    type=str,
                    help="End date for reporting in dd/mm/yyyy format")
parser.add_argument('--incident_file',
                    type=str,
                    help="Path to incidents file")
parser.add_argument("--area_file",
                    type=str,
                    help="Path to area file")
parser.add_argument("--victims_file",
                    type=str,
                    help="Path to victims file")
parser.add_argument("--location_file",
                    type=str,
                    help="Path to latlong.json file")
parser.add_argument("--get_incidents",
                    type=bool,
                    help='''Boolean flag for finding the number of incidents
                    in a given date range or for whole of data''')
parser.add_argument("--plot_incidents",
                    type=bool,
                    help='''Boolean weather plot for all the incidents over time
                    needs to be created''')
parser.add_argument('--incidents_area',
                    type=bool,
                    help='''Boolean to find the number of incidents 
                    in an area. You may need to provide additional
                    date range information''')
parser.add_argument("--plot_heatmap_areas",
                    type=bool,
                    help='''Boolean flag to plot heatmap of 
                    incidents and area, optional list of 
                    areas and incidents can be given using 
                    --area_list and --year_list arguments''')
parser.add_argument("--get_avg_age",
                    type=bool,
                    help='''Boolean flag to compute avg age
                    of victims, one can use the optional flag
                    --area as well to filter by area''')
parser.add_argument("--plot_avg_age",
                    type=bool,
                    help='''Boolean flag to plot avg age of victims,
                    one can use the optional flag --area as well''')
parser.add_argument("--plot_dist_age",
                    type=bool,
                    help='''Boolean flag to plot age distribution 
                    of victims. Optional flag --year_list can be added''')
parser.add_argument("--plot_year_area",
                    type=bool,
                    help='''Boolean to plot heatmap avg age of 
                    victims across area and years. Optional args --year_list
                    abd --area_list can be provided''')
parser.add_argument("--area",
                    type=str,
                    help='''Name of area in the area file''')
parser.add_argument("--area_list",
                     type=list,
                     help='''List of areas to plot''')
parser.add_argument("--year_list",
                    type=list,
                    help='''List of years to plot''')
parser.add_argument("--incident_date",
                    type=str,
                    help='''Optional argument, needed for 
                    computing haversine distance for a given location.
                    To be used in conjunction with --compute_avg_dist''')
parser.add_argument("--compute_avg_dist",
                    type=bool,
                    help='''Boolean to compute avg distance.
                    To be used with --area and optional parameter
                    --incident_date''')
parser.add_argument("--plot_avg_distance",
                    type=bool,
                    help='''Boolean to plot avg distance of incidents
                    across areas''')
parser.add_argument("--year",
                    type=str,
                    help='''Year for which distance across areas is to
                    be computer. Format yyyy''')
if __name__=="__main__":
    args = vars(parser.parse_args())
    path_csv_dq = args.get('path_csv_dq')
    incidents_file = args.get('incidents_file')
    areas_file = args.get('areas_file')
    victims_file = args.get('victims_file')
    location_file = args.get("location_file")
    get_incidents = args.get('get_incidents')
    plot_incidents = args.get('plot_incidents')
    incidents_area = args.get('incidents_area')
    start_date = args.get('start_date')
    end_date = args.get('end_date')
    area = args.get('area')
    plot_heatmap_areas = args.get('plot_heatmap_areas')
    area_list = args.get('area_list')
    year_list = args.get('year_list')
    get_avg_age = args.get('get_avg_age')
    plot_avg_age = args.get('plot_avg_age')
    plot_dist_age = args.get('plot_dist_age')
    plot_year_area = args.get('plot_year_area')
    incident_date = args.get('incident_date')
    location_file = args.get('location_file')
    compute_avg_dist = args.get('compute_avg_dist')
    plot_avg_distance = args.get('plot_avg_distance')
    year = args.get('year')
    if path_csv_dq is not None:
        generate_dq_report(path_csv_dq)
    ## Use only the Incident Class
    if incidents_file and areas_file:
        inc = incidents.Incidents(incidents_file,areas_file)
        if get_incidents:
            find_incidents(inc,start_date,end_date)
        if plot_incidents:
            create_plot_incidents(inc)
        if incidents_area:
            incidents_area_date_range(inc,area,start_date,end_date)
        if plot_heatmap_areas:
            plot_heatmapAreas(inc,area_list,year_list)
    ## Use only the Victims Class
    if incidents_file and areas_file and victims_file:
        v = victims.Victims(incidents_file,victims_file,areas_file)
        if get_avg_age:
            find_avg_age(v,area)
        if plot_avg_age:
            plot_avgAge(v,area)
        if plot_dist_age:
            plot_distAge(v,year_list)
        if plot_year_area:
            plot_yearArea(v,year_list,area_list)
    ## Use only the location class
    if incidents_file and location_file and areas_file:
        l = locations.Location(incidents_file,location_file,areas_file)
        if compute_avg_dist and area:
            compute_avgDist(l,area,incident_date)
        if plot_avg_distance and year:
            plot_avgDist(l,year)
            

        

