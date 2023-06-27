/*p3*/
select count(*) from oscar_nominees
where nominee='Abigail Breslin';

/*p4*/
SELECT part,assembly_step FROM parts_assembly
where finish_date IS NULL

/*p5*/
with t2 as (
with t1 as(
SELECT *, extract(year from tweet_date) as yr FROM tweets
where extract(year from tweet_date)=2022)
select user_id,count(*) as cnt from t1
group by user_id)
select cnt as tweet_bucket, count(*) as users_num from t2
group by cnt;

/*p6*/
SELECT sender_id, count(*) as message_count FROM messages
where extract(year from sent_date)=2022 and extract(month from sent_date)=8
group by sender_id 
order by message_count desc
limit 2;


/*p8*/
SELECT extract(month from submit_date) as mth,product_id as product,
round(AVG(stars),2) as avg_stars from reviews
group by mth,product
order by mth,product

