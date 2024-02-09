import os
import logging
from read import read_all_tables_from_mysql
from write import write_all_tables_to_postgres
from config import DB_DETAILS

#Logging configuration
logging.basicConfig(filename='etl.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s' )


def main():
    """ Main function to orchestrate the ETL process"""
    try:
        logging.info("Starting the ETL Process")
        mysql_dfs = read_all_tables_from_mysql()

        write_all_tables_to_postgres(mysql_dfs)
        logging.info("ETL Process completed sucessfully")

    except Exception as e:
        logging.error(f"Error in the ETL process: {e}")
        raise



if __name__ == '__main__':
    main()



