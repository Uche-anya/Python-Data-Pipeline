# util.py
import logging
import mysql.connector
import psycopg2
from config import DB_DETAILS

#Configure logging
logging.basicConfig(filename='etl.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s' )
#Logger instance
logger = logging.getLogger('mylogger')

def get_mysql_connection():
    """Establish a connection to MySQL database."""
    try:
        source_db_config = DB_DETAILS['dev']['SOURCE_DB']
        return mysql.connector.connect(
            host=source_db_config['DB_HOST'],
            database=source_db_config['DB_NAME'],
            user=source_db_config['DB_USER'],
            password=source_db_config['DB_PASS']
        )
    except mysql.connector.Error as e:
        logging.error(f"Error connecting to MySQL database: {e}")
        return None

def get_postgres_connection():
    """Establish a connection to PostgreSQL database."""
    try:
        target_db_config = DB_DETAILS['dev']['TARGET_DB']
        return psycopg2.connect(
            host=target_db_config['DB_HOST'],
            database=target_db_config['DB_NAME'],
            user=target_db_config['DB_USER'],
            password=target_db_config['DB_PASS']
        )
    except psycopg2.Error as e:
        logging.error(f"Error connecting to PostgreSQL database: {e}")
        return None


