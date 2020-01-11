
from etl import etl_process
from db_credentials import datawarehouse_db_config, sqlserver_db_config
from sql_queries import sqlserver_queries
from variables import DW_name
import pyodbc

# This Application's purpose is to get data from one SQL Server DB,
# transform it and load it in a second SQL Server DB (our "DW").
# I know the SQL queries in order to fetch, transform and load the data can get really complicated,
# but for the purpose of this example I will be using really simple SQL statements.

def main():
    print('Starting ETL')

    # Establish connection for target database (SQL-Server "DW")
    dw_cnx = pyodbc.connect(*datawarehouse_db_config)

    # Execute ETL
    for config in sqlserver_db_config:
        try:
            print("Loading DB")
            etl_process(sqlserver_queries, dw_cnx, config, 'sqlserver')

        except Exception as error:
            print("etl for database has error")
            print('error message: {}'.format(error))
        finally:
            dw_cnx.commit()
            dw_cnx.close()


if __name__ == "__main__":
    main()