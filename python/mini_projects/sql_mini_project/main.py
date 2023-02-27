import os
import logging
from bulk_load import utils, config,sql
logging.basicConfig(level=logging.INFO,format = '%(asctime)s %(levelname)s - %(message)s')
data_dir_path = "./data"

file_table_mapping = (
    ('region.csv','region'),
    ('sales_rep.csv','sales_rep'),
    ('accounts.csv','accounts'),
    ('web_events.csv','web_events'),
    ('orders.csv','orders')
)


if __name__=="__main__":
    logging.info("Establishing connection to default database")
    conn_default = utils.connect_db(dbname=config.dbname_default,
                            user=config.user,
                            password=config.password,
                            port=config.port,
                            host=config.host)
    conn_default.set_session(autocommit=True)
    curr = conn_default.cursor()
    logging.info("Creating new database.")
    curr.execute(sql.create_db)
    curr.close()
    conn_default.close()

    conn = utils.connect_db(dbname=config.dbname_created,
                            user=config.user,
                            password=config.password,
                            port=config.port,
                            host=config.host)
    conn.set_session(autocommit=True)
    curr = conn.cursor()
    logging.info("Creating tables")
    for table_query in sql.create_tables:
        curr.execute(table_query)
        logging.info(f"Created table with query {table_query}")
    
    for file_name,table_name in file_table_mapping:
        path = os.path.join(data_dir_path,file_name)
        with open(path,'r') as f:
            curr.copy_expert(f"COPY {table_name} FROM STDIN WITH HEADER CSV",f)
            logging.info(f"Copied data from {path},{table_name}")
    curr.close()
    conn.close()
