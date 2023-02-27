import psycopg2

def connect_db(dbname,user,password,host,port):
    conn = psycopg2.connect(dbname=dbname,
                            user=user,
                            password=password,
                            host=host,
                            port=port)
    return conn
