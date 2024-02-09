
from util import get_postgres_connection

def write_to_postgres(table_name, data, batch_size=100):
    """ Write data to PostgresSQL table"""
    connection = get_postgres_connection()
    cursor = connection.cursor()
    try:
        for i in range(0, len(data), batch_size):
            batch = data[i:i + batch_size]
            insert_query = f" INSERT INTO {table_name} VALUES ({','.join(['%s'] * len(data[0]))})"
            cursor.executemany(insert_query, batch)
            connection.commit()
    finally:
        cursor.close()
        connection.close()

def write_all_tables_to_postgres(tables_data, batchsize=100 ):
    """ Write data from all tables to Postgresql"""
    for table_name, data in tables_data.items():
        write_to_postgres(table_name, data, batchsize)

