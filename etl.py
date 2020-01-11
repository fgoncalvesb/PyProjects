# Python modules used
import pyodbc

# variables
from variables import DW_name


def etl(query, source_cnx, target_cnx):
    # extract data from source db
    source_cursor = source_cnx.cursor()
    source_cursor.execute(query.extract_query)
    data = source_cursor.fetchall()
    source_cursor.close()

    # load data into warehouse db
    if data:
        target_cursor = target_cnx.cursor()
        target_cursor.execute("USE {}".format(DW_name))
        target_cursor.executemany(query.load_query, data)
        print(data)
        print('Data loaded to warehouse db')
        target_cursor.close()
    else:
        print('Data is empty')

def etl_process(queries, target_cnx, source_db_config, db_platform):
        # establish source db connection
        if db_platform == 'sqlserver':
         source_cnx = pyodbc.connect(source_db_config)
        else:
            return 'Error!, unrecognised db platform'

        # loop through sql queries
        for query in queries:
            etl(query, source_cnx, target_cnx)


          # close the source db connection
        source_cnx.close()