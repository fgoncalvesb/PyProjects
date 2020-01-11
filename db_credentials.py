from variables import DW_name

# In this case, I had to previously create the user, define it's password and grant him the proper access in each DB
# I'm using my pc as local server

# sql-server (source db)
sqlserver_db_config = {
    'Driver={SQL Server};'
    'Server=DESKTOP-S9J69RQ\SQLEXPRESS;'
    'Database=workdb_01;'
    'Uid=john;'
    'pwd=1234;'
    'Trusted_Connection=no;'
  }

# sql-server (target db, our "DW")
datawarehouse_db_config = {
                      'Driver={SQL Server};'
                      'Server=DESKTOP-S9J69RQ\SQLEXPRESS;'
                      'Database=local_DW;'
                      'Uid=john;'
                      'pwd=1234;'
                      'Trusted_Connection=no;'
}