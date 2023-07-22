/*Windowdb*/
/*1*/
select *,
lag(sold) over (
PARTITION by fruit order by date(month)
) as next 
from fruitmart;
/*2*/
select *,
lead(sold) over (
PARTITION by fruit order by date(month)
) as next 
from fruitmart;
/*3 a*/
with lagged_table as (
select *,
lag(sold) over (
PARTITION by fruit, date(month)
order by date(month)
) as previous 
from fruitmart
)
select *, (previous-sold)/sold  as perc_change from lagged_table;
/*3 b*/
with lagged_table as (
select *,
lag(sold) over (
PARTITION by fruit, date(month)
order by date(month)
) as previous 
from fruitmart
)
select *, round(cast((previous-sold) as Real)/cast(sold as REAL), 3) as perc_change from lagged_table;

/*4*/
select * ,
sum(sold) over (PARTITION BY fruit, month
order by date(month)
ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
) as running_total
from fruitmart
/*5*/
select * ,
sum(sold) over (PARTITION BY fruit, date(month)
order by date(month)
ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING
) as moving_total
from fruitmart

/*example db sales*/
with diff_table as (
with consolidated_table as (
	with sub_table as (
	select *, cast(strftime("%Y",sales_month)  as INTEGER)  as Year
	from sales 
	where kind_of_business="Men's clothing stores"
	)
	select Year, sum(sales) as tot_sales
	from sub_table
	group by Year
	order by Year 
)
select *,
tot_sales - lag(tot_sales) over(order by Year) as diff
 from consolidated_table
)
select *, round(cast(diff as REAL)/cast(tot_sales as REAL)*100 ,2)as pct_change from diff_table;

/*Union*/
/*1*/
SELECT t2.product_name
FROM order_01_2021 AS t1
LEFT JOIN product AS t2 ON t1.product_id = t2.product_id
UNION
SELECT t2.product_name
FROM order_02_2021 AS t1
LEFT JOIN product AS t2 ON t1.product_id = t2.product_id;
/*2*/
SELECT t1.order_id,
       t1.quantity,
       t2.product_name,
       t2.list_price
FROM order_01_2021 AS t1
LEFT JOIN product AS t2 ON t1.product_id = t2.product_id
UNION ALL
SELECT t1.order_id,
       t1.quantity,
       t2.product_name,
       t2.list_price
FROM order_02_2021 AS t1
LEFT JOIN product AS t2 ON t1.product_id = t2.product_id;
/*datalemur*/
/*1*/
WITH yearly_spend_cte AS (
  SELECT 
    EXTRACT(YEAR FROM transaction_date) AS yr,
    product_id,
    spend AS curr_year_spend,
    LAG(spend) OVER (
      PARTITION BY product_id 
      ORDER BY 
        product_id, 
        EXTRACT(YEAR FROM transaction_date)) AS prev_year_spend 
  FROM user_transactions
)

SELECT 
  yr,
  product_id, 
  curr_year_spend, 
  prev_year_spend, 
  ROUND(100 * 
    (curr_year_spend - prev_year_spend)
    / prev_year_spend
  , 2) AS yoy_rate 
FROM yearly_spend_cte;
/*2*/
WITH payments AS (
  SELECT 
    merchant_id, 
    EXTRACT(EPOCH FROM transaction_timestamp - 
      LAG(transaction_timestamp) OVER(
        PARTITION BY merchant_id, credit_card_id, amount 
        ORDER BY transaction_timestamp)
    )/60 AS minute_difference 
  FROM transactions) 

SELECT COUNT(merchant_id) AS payment_count
FROM payments 
WHERE minute_difference <= 10;