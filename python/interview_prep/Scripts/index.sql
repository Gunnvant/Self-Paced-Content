create database dwh;

create table cust_info (
cust_id int,
first_name varchar(30),
address varchar(100),
constraint cust_idf
primary key (cust_id,first_name) /*Primary keys will have a clsutered index*/
) engine=InnoDB;


create table emp_info(
emp_id int,
first_name varchar(30),
address varchar(100)
)

CREATE INDEX emp_index ON emp_info (emp_id ASC);  /* creates a non clustered index*/