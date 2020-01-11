# The transformation SQL functions or filters have to be included in the extract query.

sqlserver_extract = ('''
  SELECT * from Empleados
''')

sqlserver_insert = ('''
  INSERT INTO Empleados
  VALUES (?, ?, ?, ?)  
''')

# I create a class in case I eventually need to get the information from different sources that use SQL, apart from
# a db in SQL-Server.

class SqlQuery:
    def __init__(self, extract_query, load_query):
        self.extract_query = extract_query
        self.load_query = load_query


# I create the instance for SQLServer
sqlserver_query = SqlQuery(sqlserver_extract, sqlserver_insert)

# I store it as list for iteration
sqlserver_queries = [sqlserver_query]