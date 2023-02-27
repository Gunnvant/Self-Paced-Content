create_tables = [
'''create table REGION(
ID INT,
NAME VARCHAR,
primary key (ID)
);''',
'''
create table SALES_REP(
ID INT,
NAME VARCHAR,
REGION_ID INT,
primary key (ID),
constraint SALESREP_FK 
	foreign key(region_id)
		references region(ID)
);
''',
'''
create table ACCOUNTS (
ID INT,
NAME VARCHAR,
WEBSITE VARCHAR,
LAT FLOAT,
LONG FLOAT,
PRIMARY_POC VARCHAR,
SALES_REP_ID INT,
primary key (ID),
constraint ACCOUNTS_FK
	foreign key(SALES_REP_ID)
		references SALES_REP(ID)
);
''',
'''
create table WEB_EVENTS (
ID INT,
ACCOUNT_ID INT,
OCCURED_AT TIMESTAMP,
CHANNEL VARCHAR,
primary key (ID),
constraint webevents_fk
	foreign key(ACCOUNT_ID)
		references ACCOUNTS(ID)
);
''',
'''
create table ORDERS (
ID INT,
ACCOUNT_ID INT,
OCCURED_AT TIMESTAMP,
STANDARD_QTY INT,
GLOSS_QTY INT,
POSTER_QTY INT,
TOTAL INT,
STANDARD_AMT_USD FLOAT,
GLOSS_AMT_USD FLOAT,
POSTER_AMT_USD FLOAT,
TOTAL_AMT_USD FLOAT,
primary key (ID),
constraint ORDERS_FK
	foreign key(ACCOUNT_ID)
		references ACCOUNTS(ID)
);
'''
]

create_db = '''
create database dwh;
'''