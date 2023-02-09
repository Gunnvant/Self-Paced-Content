## Bulk Inserts
Its good to use `insert` statements to get data inside a database. For small data loads `insert` statements are a good choice. If you want to load a very large file in the database then you have two options:

1. Use a bulk loading utility. For example postgres has `copy` and mysql has `dump`
2. Use a python driver to call the `copy` or `dump` functionality

[**Bulk Load Demo Postgres**](src)

We will use the data [link](./data/health-facilities-gh.csv) to show how bulk insert works and will also show how to bulk unload the data.

- Step 1: Create table in the database

```sql
create table if not exists health_facilities(
Region varchar,
District varchar,
FacilityName varchar,
Kind varchar, 
Town varchar,
Type_Ownership varchar,
Latitude float,
Longitude float    
)
```
- Step 2.1: Now use the bulk upload command (relevant for `postgres`)
Postgres supports `\copy` for bulk data uploads via `psql` utility.

For example to load the file `health_facilities_gh.csv` we can run the following command on `psql`

```sql
\copy health_facilities from '/Users/gunnvantsaini/Library/CloudStorage/OneDrive-Personal/Work/Vired/Content/self_paced/code_repo/python/interview_prep/sql/bulk_load/data/health_facilities_gh.csv' WITH DELIMITER ',' CSV HEADER;
```

- Step 2.2: Use python driver to do bulk data load.

Create a python environment where `psycopg2` is installed. Use the `env.yaml` file to create the python environment. Run the following command

```shell
conda env create -f env.yaml
conda activate sql_dump

```

Now we can construct a small python script to do the bulk loading of the same dataset we have seen earlier.

We can use the `main.py` file to run the bulk insert program. Change the file `./src/config.py` with appropriate values of `host`, `user`, `password` etc.

The main loading logic is in file `./src/load.py`. See the function `dump_data()`