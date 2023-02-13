## Inserts and dealing with conflicts.

Upserts (a combination of "update" and "insert") are required in scenarios where you need to either update an existing record in a database or insert a new record if it doesn't already exist.

For example, consider a customer relationship management (CRM) system that needs to keep track of customer information. Each customer has a unique customer ID, which is used as the primary key in the database. If a customer's information changes (e.g., their address), the CRM system needs to update the existing record for that customer. However, if a new customer is added to the system, a new record needs to be inserted.

In this scenario, an upsert operation would be used to ensure that the customer's information is either updated or inserted, as appropriate. This would eliminate the need to check whether the customer record already exists before performing the update or insert operation, and would save time and resources compared to using separate update and insert operations.

**Example**
Imagine we have the following table defined:

```sql
CREATE TABLE CUSTOMER (
    ID INT,
    FIRST_NAME VARCHAR,
    LAST_NAME VARCHAR,
    ADDRESS VARCHAR,
    AGE FLOAT,
    PRIMARY KEY (ID)

)
```
Now let's insert the following data

```sql
INSERT INTO CUSTOMER VALUES 
(1,'ADAM','SMITH', '9 AND QUARTERS, HEMMING LANE',45),
(2,'SAD','SMITH', '9 AND HALF, HEMMING LANE',47),
(3,'ADAM','SANDLER', '9, HEMMING LANE',48);
```

Now imagine that the address for the customer with id 1 changes, how can we update this record. If we try to run the following code we will receive an error.

```sql
INSERT INTO CUSTOMER VALUES 
(1,'ADAM','SMITH', 'New address',45);
```

To rectify the error encountered in the above piece of code one can write an upsert query see the following example (`postgres`)

```sql
INSERT INTO CUSTOMER VALUES
(1,'ADAM','SMITH', 'New address',45)
ON CONFLICT (ID)
DO
    UPDATE SET ADDRESS=EXCLUDED.ADDRESS

```

One can do something similar in `mysql` as well

```sql
create database dwh;

CREATE TABLE dwh.CUSTOMER (
    ID INT,
    FIRST_NAME VARCHAR(20),
    LAST_NAME VARCHAR(20),
    ADDRESS VARCHAR(100),
    AGE FLOAT,
    PRIMARY KEY (ID));

INSERT INTO dwh.CUSTOMER VALUES 
(1,'ADAM','SMITH', '9 AND QUARTERS, HEMMING LANE',45),
(2,'SAD','SMITH', '9 AND HALF, HEMMING LANE',47),
(3,'ADAM','SANDLER', '9, HEMMING LANE',48);

INSERT INTO dwh.CUSTOMER VALUES
(1,'ADAM','SMITH', 'NEW ADDRESS',45)
ON DUPLICATE KEY UPDATE ADDRESS = 'NEW ADDRESS';
```
