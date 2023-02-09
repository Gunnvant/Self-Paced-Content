from src import load,config
import logging 
logging.basicConfig(level=logging.INFO,format = '%(asctime)s %(levelname)s - %(message)s')

if __name__=='__main__':
    logging.info(f'Starting bulk upload of file {config.file_path} to table {config.tablename}')
    load.dump_data()
    logging.info("Data loaded to the table")