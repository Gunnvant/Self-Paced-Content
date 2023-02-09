import psycopg2
import src.config as config

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

