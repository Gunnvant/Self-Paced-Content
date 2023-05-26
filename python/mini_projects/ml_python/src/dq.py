import pandas as pd
from __future__ import annotations

class DataQuality():
    def __init__(self,path_csv_file):
        self.path_csv_file = path_csv_file

    def _create_dq_numeric_vars(self):
        '''
        This generates a data frame with data
        quality metrics for all the numeric variables
        in the data. The df will have the following columns:
        - var_name: name of the variable in original df, this is 
                    a numeric var
        - mean: the average of the var
        - std_dev: the standard deviation of the var
        - num_zeroes: number of values equal to zero in the var
        - pct_zeroes: percent of values that are equal to zero
        - num_missing_values: number of missing values in the var
        - pct_missing_values: percent of missing values in the var that are missing
        - num_unique: number of unique values
        - min: the minimum value
        - p5: the fifth percentile value
        - p25: the 25th percentile value
        - p50: the 50th percentile value
        - p75: the 75th percentile value
        - p90: the 90th percentile value
        - p95: the 95th percentile value
        - p99: the 99th percentile value
        - max: the maximum value
        '''
        ## Place your code here
        pass

    def _create_dq_categorical_var(self):
        '''
        This generates a data frame which will contain the 
        data quality report for categorical variables. This
        data frame will have the following columns:

        - var_name: name of the categorical variable col
        - num_unique_vals: number of unique values of the
                           categorical variable
        - num_missing: number of missing values
        - pct_missing: pct of missing values
        '''
        ## Place your code here
        pass
    def create_dq(self):
        '''
        This will call:

        1. _create_dq_numeric_vars  to produce df1
        2. _create_dq_categorical_var to produce df2

        Then df1 and df2 will be returned
        '''
        ## Place your code here
        pass
        return df1,df2