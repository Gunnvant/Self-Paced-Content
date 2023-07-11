## Joins
Use the dataset `customer.csv` and `sales.csv`

### Drill Examples

1. Which types of customer has high average customer rating ?
2. Find out total sales based on branch and sort it in descending order.
3. Filter as per below criteria and find out the total quantity ordered based on customer type.

Filter the Females who use Health and beauty products and male who uses Sports and travel

## Self Join

### Drill example

```sql
select t1.id,t1.sku,t2.id,t2.sku from inventory t1,inventory t2
where t1.id=t2.id
```

### In class problem

Find the employees who earn more than their managers

```sql
create table emp (
Id int,
Name varchar,
Salary int,
ManagerId int
);

insert into emp VALUES
(1,"Joe",7000,3),
(2,"Henry",8000,4),
(3,"Sam",6000,NULL),
(4,"Max",9000,NULL);
```

## Case Statements

1. Use the dataset `churn.csv`  and do the following:
    - Create a new column that bins the Monthly charges column in to high medium and low. A monthly charge of equal to or over 100 is considered high, less than 100 and more than or equal to 70 is considered medium and rest are considered low.
    - Do the same exercise on the column tenure. A tenure of more than or equal to 50 is considered high, less than 50 to greater than equal to 30 is considered medium and less than 30 is considered low.
    - Pivot the data and show average tenure by phone service. The table should have the following format:

| PhoneService_Yes| Phoneservice_No |
| :---------------|----------------- |
| Avg1 | Avg2                        |

- Do the same pivot for Payment Method column and find the relative percentage of monthly charges for each method.


## Data Lemur Problems

## Problem 1 [link](https://datalemur.com/questions/laptop-mobile-viewership)
Given a table of candidates and their skills, you're tasked with finding the candidates best suited for an open Data Science job. You want to find candidates who are proficient in Python, Tableau, and PostgreSQL.

Write a query to list the candidates who possess all of the required skills for the job. Sort the output by candidate ID in ascending order.

**Assumption:**

There are no duplicates in the candidates table.

**candidates Table:**

| Column Name  | Type    |
| :----------- | :------ |
| candidate_id | integer |
| skill        | varchar |

**candidates Example Input:**

| candidate_id | skill      |
| :----------- | :--------- |
| 123          | Python     |
| 123          | Tableau    |
| 123          | PostgreSQL |
| 234          | R          |
| 234          | PowerBI    |
| 234          | SQL Server |
| 345          | Python     |
| 345          | Tableau    |

**Example Output:**

| candidate_id |
| :----------- |
| 123          |

Explanation
Candidate 123 is displayed because they have Python, Tableau, and PostgreSQL skills. 345 isn't included in the output because they're missing one of the required skills: PostgreSQL.

The dataset you are querying against may have different input & output - this is just an example!

## Problem 2 [link](https://datalemur.com/questions/laptop-mobile-viewership)

Write a query that calculates the total viewership for laptops and mobile devices where mobile is defined as the sum of tablet and phone viewership. Output the total viewership for laptops as laptop_reviews and the total viewership for mobile devices as mobile_views.

Effective 15 April 2023, the solution has been updated with a more concise and easy-to-understand approach.

**viewership Table**

| Column Name | Type                                 |
| :---------- | :----------------------------------- |
| user_id     | integer                              |
| device_type | string ('laptop', 'tablet', 'phone') |
| view_time   | timestamp                            |

**viewership Example Input**

| user_id | device_type | view_time           |
| :------ | :---------- | :------------------ |
| 123     | tablet      | 01/02/2022 00:00:00 |
| 125     | laptop      | 01/07/2022 00:00:00 |
| 128     | laptop      | 02/09/2022 00:00:00 |
| 129     | phone       | 02/09/2022 00:00:00 |
| 145     | tablet      | 02/24/2022 00:00:00 |

**Example Output**

| laptop_views | mobile_views |
| :----------- | :----------- |
| 2            | 3            |

Explanation
Based on the example input, there are a total of 2 laptop views and 3 mobile views.

The dataset you are querying against may have different input & output - this is just an example!
