from util import get_mysql_connection

def read_from_mysql(table_name):
    """ Read data from mysql table"""
    # Establishing a connection to the MySQL database
    connection = get_mysql_connection()
    cursor = connection.cursor()
    query = f"SELECT * FROM {table_name}"
    cursor.execute(query)
    data = cursor.fetchall()
    cursor.close()
    connection.close()
    return data

def read_all_tables_from_mysql():
    """ Read data from all MySQL tables"""
    tables = [ "customers", "orders", "departments", "categories", "order_items", "products"]
    tables_data = {}
    for table in tables:
        tables_data[table] = read_from_mysql(table)
    return tables_data
