## SQL Practice Day 2

**Learning Objectives**:
- Be able to create schema for a database from a description
- Apply foreign and primary key constraints
- Be able to use self joins to answer business questions
- Be able to use common window functions to answer common business questions

## Drill Problem
How to create constraints and create a database

```sql
/*Tested on sqlite3*/
create table Region(
id int,
name varchar,
PRIMARY KEY(id)
);

create table Sales_Rep(
id int,
name varchar,
region_id int,
PRIMARY KEY(id),
CONSTRAINT SALESREP_FK
	FOREIGN KEY(region_id)
		REFERENCES Region(id)
);
```
Insert the data in the table Region

```sql
insert into Region values 
(1,"North"),
(2,"East"),
(3,"West"),
(4,"South")
;
```

Insert data in table Sales_Rep

```sql
insert into Sales_Rep values 
(1,"John",1),
(2,"Ron",1),
(3,"Linda",2),
(4,"Kinda",2),
(5,"Belinda",3),
(6,"Mona",4),
(7,"Yona",4),
(8,"Gonna",4);
```

## In Class Problem

Create a tables:

- Inventory
- Transactions
- Customer

## Sub Query Practice

Use dataset employee_db_new
**p1**

Find out the list of employees whose salary is more than Bharath

**p2**

Find out the list of employees whose salary is more than Jitendra and less than Ajay Kumar

**p3**

Find the % of Mouna’s CTC from her team’s total sum of CTC.

**p4**

Find the % of employee’s CTC from their team’s total sum of CTC.


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

## Window Functions Practice

**P1**

Rank the employees of each team based on their performance


**P2**
Rank them based on designation level

**P3** 

Find the minimum salary in each designation level 

## DataLemur Problems

## p1 [link](https://datalemur.com/questions/duplicate-job-listings)

Assume you're given a table containing job postings from various companies on the LinkedIn platform. Write a query to retrieve the count of companies that have posted duplicate job listings.

Definition:

Duplicate job listings are defined as two job listings within the same company that share identical titles and descriptions.

job_listings Table:

| Column Name | Type    |
| :---------- | :------ |
| job_id      | integer |
| company_id  | integer |
| title       | string  |
| description | string  |

job_listings Example Input:

| job_id | company_id | title            | description                                                                                                                                                                              |
| :----- | :--------- | :--------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 248    | 827        | Business Analyst | Business analyst evaluates past and current business data with the primary goal of improving decision-making processes within organizations.                                             |
| 149    | 845        | Business Analyst | Business analyst evaluates past and current business data with the primary goal of improving decision-making processes within organizations.                                             |
| 945    | 345        | Data Analyst     | Data analyst reviews data to identify key insights into a business's customers and ways the data can be used to solve problems.                                                          |
| 164    | 345        | Data Analyst     | Data analyst reviews data to identify key insights into a business's customers and ways the data can be used to solve problems.                                                          |
| 172    | 244        | Data Engineer    | Data engineer works in a variety of settings to build systems that collect, manage, and convert raw data into usable information for data scientists and business analysts to interpret. |
|        |            |                  |                                                                                                                                                                                          |
Example Output:

| duplicate_companies |
| :------------------ |
| 1                   |
|                     |

Explanation:
There is one company ID 345 that posted duplicate job listings. The duplicate listings, IDs 945 and 164 have identical titles and descriptions.

The dataset you are querying against may have different input & output - this is just an example!

## Problem 2 [link](https://datalemur.com/questions/laptop-mobile-viewership)
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

## Problem 3 [link](https://datalemur.com/questions/laptop-mobile-viewership)

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
