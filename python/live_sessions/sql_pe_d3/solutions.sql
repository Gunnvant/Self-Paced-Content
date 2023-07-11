/*Self Join*/
/*Self Join-In Class*/
select t1.Id,t1.Name,t1.Salary,t1.ManagerId,t2.Id,t2.Name,t2.Salary,t2.ManagerId from emp t1, emp t2
where t1.ManagerId=t2.Id
and t1.Salary>t2.Salary

/*Case Statements*/
/*p1*/
select *,
case 
	when MonthlyCharges>=100 then "high"
	when MonthlyCharges<100 and MonthlyCharges>=70 then "medium"
	else "low"
end as monthly_partition
from churn;
/*p2*/
select *,
case 
	when Tenure>=50 then "high"
	when Tenure<50 and Tenure>=30 then "medium"
	else "low"
end as tenure_bins
from churn;
/*p3*/

SELECT
avg(case 
	when PhoneService="Yes" then MonthlyCharges else NULL
end) as PhoneService_Yes,
avg(CASE
	when PhoneService="No" then MonthlyCharges else NULL
end) as PhoneService_No
from churn;

/*p4*/
with t1 as (
select sum(MonthlyCharges) as tot_charges,
sum(CASE	
	when PaymentMethod="Electronic check" then MonthlyCharges else NULL
end) as Electronic_Check,
sum(CASE	
	when PaymentMethod="Mailed check" then MonthlyCharges else NULL
end) as Mailed_Check,
sum(CASE	
	when PaymentMethod="Bank transfer (automatic)" then MonthlyCharges else NULL
end) as Bank_transfer,
sum(CASE	
	when PaymentMethod="Credit card (automatic)" then MonthlyCharges else NULL
end) as Credit_Card
from churn)
select Electronic_Check/tot_charges, Mailed_Check/tot_charges,Bank_transfer/tot_charges,
Credit_Card/tot_charges from t1;


/*Data Lemur Problems*/

/*p1*/
with t1 as (
SELECT candidate_id, 
sum(case 
    when skill in ('Python','Tableau','PostgreSQL') then 1 else 0
end)
as ind
FROM
candidates 
GROUP BY candidate_id
)
select candidate_id from t1 where ind=3
order by candidate_id

/*p2*/
SELECT
sum(CASE
    when device_type = 'laptop' then 1 else 0
END) as laptop_views,
sum(CASE
    when device_type <> 'laptop' then 1 else 0
END) as mobile_views
FROM viewership;
