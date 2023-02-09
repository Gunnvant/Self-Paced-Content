import psycopg2
import src.config as config

user = config.user
pw = config.password
port = config.port
host = config.host
dbname = config.dbname
file_path = config.file_path
table_name = config.tablename

def dump_data(config=config):
    conn = psycopg2.connect(dbname = config.dbname,
                            user = config.user,
                            password = config.password,
                            host = config.host,
                            port = config.port)
    curr = conn.cursor()
    with open(config.file_path,'r') as f:
        curr.copy_expert(f"COPY {config.tablename} FROM STDIN WITH HEADER CSV",f)
        conn.commit()
        conn.close()

