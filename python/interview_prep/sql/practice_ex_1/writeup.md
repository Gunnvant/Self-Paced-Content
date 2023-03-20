## Time Series Analysis of Retail Data

Time series analysis is one of the most common types of analysis done with SQL. A time series is a sequence of measurements or data points recorded in time order, often at regularly spaced intervals.

In retail space, its very important to be able to work with time series data. Most transaction data is inevitably time series in nature as every transaction has a timestamp associated with it.

In this exercise you will be answering some business questions based on retail sales data. 

#### Data 
Use the dataset [`retail_sales.csv`](retail_sales.csv). Load it into an sql engine of your choice (`sqlite`,`postgres` or `mysql`).

You need to create a table known as `retail_sales`. The table should contain the following columns

- sales_date 
- naics_code 
- kind_of_business 
- reason_for_null
- sales

#### Tasks

Task 1(a): Create the table in your sql engine with appropriate data types.

Task 1(b): Do a bulk upload of the data using an appropriate command

## Task 2
A potential investor is looking to invest in the retail business whose dataset you are currently working on.

The investor needs to understand which product categories the business is good at. Can you do a historical analysis of revenue share of each product line to identify product lines that have more revenue share.

## Task 3
One of the product lines the investor is interested in is `Women's clothing stores` and `Men's clothing stores`. The investment firm wants to understand what is the relative size of both the businesses.

## Task 4
Another dimension that the investor is interested in is, finding out which product categories are growing since the past 10 years. Can you help them with this task?

## Submission Instructions

You need to submit your sql queries in as an sql file. Each task should have properly commented code.