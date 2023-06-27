/*Constraints In Class Ex*/
create table inventory (
id int,
sku varchar,
price NUMERIC,
PRIMARY KEY(id))

create table customer (
id int,
name varchar,
PRIMARY KEY(id)
);

create table transactions (
id int,
qty int,
cust_id int,
inventory_id int,
PRIMARY KEY(id),
CONSTRAINT CUST_FK FOREIGN KEY(cust_id) REFERENCES customer(id),
CONSTRAINT INVENT_FK FOREIGN KEY(inventory_id) REFERENCES inventory(id)
);

insert into inventory values 
(1,"cookies",2),
(2,"bacon",3),
(3,"chicken",1.5),
(4,"turkey",3),
(5,"noodles",2);

insert into customer values 
(1,"john"),
(2,"ron"),
(3,"won"),
(4,"common");

insert into transactions VALUES
(1,3,1,1),
(2,2,1,1),
(3,5,2,3),
(4,6,3,4),
(5,2,4,5);

/*Sub Queries*/
/*P1*/
select * from employee_db_new
where AnnualCtcLpA>(select AnnualCtcLpA from employee_db_new where FirstName="BHARATH");
/*p2*/
select * from employee_db_new
where AnnualCtcLpA>(select AnnualCtcLpA from employee_db_new where FirstName="JITENDRA")
and AnnualCtcLpA<(select AnnualCtcLpA from employee_db_new where FirstName="AJAY KUMAR")
;
/*p3*/
with t1 as (
select AnnualCtcLpA as sal_m from employee_db_new
where FirstName="MOUNA"),
t2 as (
select sum(AnnualCtcLpA) as tot_sal from employee_db_new
where FirstName<>"MOUNA")
select t1.sal_m,t2.tot_sal, round(t1.sal_m/t2.tot_sal,2) as rel_sal from t1,t2;
/*p4*/
with t1 as(
select sum(AnnualCtcLpA) as tot_sal from employee_db_new),
t2 as (
select * from employee_db_new)
select round(t2.AnnualCtcLpA/t1.tot_sal,2) as rel_sal from t1,t2
/*Self Join-In Class*/
select t1.Id,t1.Name,t1.Salary,t1.ManagerId,t2.Id,t2.Name,t2.Salary,t2.ManagerId from emp t1, emp t2
where t1.ManagerId=t2.Id
and t1.Salary>t2.Salary
/*Window Functions*/
/*p1*/
select *,
rank() over(ORDER by PerformAceRating desc) as rnk 
from employee_db_new
/*p2*/
select *,
rank() over(Order by DesignationLevel desc) as rnk
from employee_db_new
/*p3*/
select *,
min(AnnualCtcLpA) over(PARTITION by DesignationLevel) as min_sal
from employee_db_new;
/*Data Lemur Problems*/
/*p1*/
with t1 as (
select company_id,title,description,
row_number() over(partition by company_id,title,description) as rnk
from job_listings)
select count(*) as duplicate_companies from t1 where rnk>1;
/*p2*/
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

/*p3*/
SELECT
sum(CASE
    when device_type = 'laptop' then 1 else 0
END) as laptop_views,
sum(CASE
    when device_type <> 'laptop' then 1 else 0
END) as mobile_views
FROM viewership;
