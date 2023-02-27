## Task 1
The tables can be loaded using `\copy` command, for this solution we've resorted to using `psycopg2` to create database as well as create tables. We have used the `copy_expert` from `psycopg2` to load the data to the database from the csv files.

The code to load tables is [here](./bulk_load/) you will need to create a python environment with the packages listed in `env.yaml`

Run the command `conda env create -f env.yaml` to create a virtual environment with the desired packages.

Then modify the file `bulk_load/config.py` with the correct values of `default_db`,`user`,`password` etc.

Finally run the command `python main.py` to create database `dwh`, tables and do bulk loading of data.

## Task 2

**2.1** One can answer this problem easily by joining the `sales_rep` and `accounts` tables. Below is the sql code to generate the desired view.

```sql
with reps_accounts as (
	select sales_rep.id as sales_rep_id,
	sales_rep."name"  as sales_rep_name,
	sales_rep.region_id as sales_rep_region,
	accounts.name as account_name
	from sales_rep
	join accounts on accounts.sales_rep_id = sales_rep.id 
)
select *,row_number() over(partition by sales_rep_name) as acc_num
from reps_accounts
order by sales_rep_region;
```

**2.2** This task can be done by writing multiple nested common table expressions. Basic steps to follow are:

1. Do appropriate joins between `orders`, `accounts` and `sales_rep` tables
2. Then Compute the yearly revenue per sales rep as well as total yearly revenue
3. Rank the percentage yearly revenue of each sales rep, year on year.

All of this can be done using the query given below:

```sql
with final_table as (
	with sales_per_rep as (
		with sales_rep_order_hist as (
			select 
			orders.total_amt_usd as tot_rev,
			orders.occured_at  as order_time,
			date_part('month',orders.occured_at) as "month", 
			date_part('year',orders.occured_at) as "year",
			accounts."name"  as account_name,
			sales_rep."name" as sales_rep_name
			from orders
			join accounts on
			orders.account_id = accounts.id 
			join sales_rep on
			sales_rep.id = accounts.sales_rep_id 
			)
		select *,
		sum(tot_rev) over (partition by year) as yearly_total,
		sum(tot_rev) over (partition by sales_rep_name,"year") as sales_rep_rev,
		sum(tot_rev) over (partition by sales_rep_name,"year")/sum(tot_rev) over (partition by "year") as perc_sales_rep
		from sales_rep_order_hist
		order by year,sales_rep_name)
	select
		"year",
		"month",
		sales_rep_name,
		perc_sales_rep,
		dense_rank() over (partition by "year" order by perc_sales_rep desc) as rank_sales_rep,
		row_number() over (partition by sales_rep_name,"year") as row_num
		from sales_per_rep)
select "year",sales_rep_name,perc_sales_rep,rank_sales_rep
from final_table
where row_num=1;

```

**2.3**

This problem can be tackled the same way as the above one, instead of doing analysis at the sales representative level. 

The code below will do the job.

```sql
with final_table as (
	with sales_per_region as (
		with sales_region_order_hist as (
			select 
			orders.total_amt_usd as tot_rev,
			orders.occured_at  as order_time,
			date_part('month',orders.occured_at) as "month", 
			date_part('year',orders.occured_at) as "year",
			region."name"  as region_name
			from orders
			join accounts on
			orders.account_id = accounts.id 
			join sales_rep on
			sales_rep.id = accounts.sales_rep_id
			join region on 
			region.id = sales_rep.region_id 
			)
		select *,
		sum(tot_rev) over (partition by year) as yearly_total,
		sum(tot_rev) over (partition by region_name,"year") as region_rev,
		sum(tot_rev) over (partition by region_name,"year")/sum(tot_rev) over (partition by "year") as perc_sales_region
		from sales_region_order_hist
		order by year,region_name)
	select
		"year",
		"month",
		region_name,
		perc_sales_region,
		dense_rank() over (partition by "year" order by perc_sales_region desc) as rank_sales_region,
		row_number() over (partition by region_name,"year") as row_num
		from sales_per_region)
select "year",region_name,perc_sales_region,rank_sales_region
from final_table
where row_num=1;
```

## Task 3
This task can be tackled by joining the `accounts` table with `orders` table. Then you will need to find out the total revenue per account for each year and finally arrive at the percent contribution to total yearly revenue.

The following query will do the trick:

```sql
with final_table as (
	with rev_acc as (
		with order_acc as (
			select 
			orders.occured_at as order_time,
			date_part('year',orders.occured_at) as "year", 
			orders.total_amt_usd  as total_rev,
			accounts."name"  as acc_name,
			accounts.id as acc_id
			from orders 
			join accounts 
			on orders.account_id = accounts.id) 
		select "year",acc_name, sum(total_rev) as rev
		from order_acc
		group by "year",acc_name
		order by "year")
	select *,
	rev/sum(rev) over (partition by "year") as pct_yearly_rev
	from rev_acc)
select *,
dense_rank() over (partition by "year" order by pct_yearly_rev desc) as rev_rank
from final_table;
```