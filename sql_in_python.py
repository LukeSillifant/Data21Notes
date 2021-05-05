import sqlalchemy

server = 'localhost,1443'
database = 'Northwind'
user = 'SA'
password = 'Passw0rd2018'
driver = 'SQL+Server'

engine = sqlalchemy.create_engine(f"mssql+pyodbc://{user}:{password}@{server}/{database}?driver={driver}")

connection = engine.connect()

result = engine.execute('SELECT * FROM Products;')
print(result)

first_row = result.fetchone()
print(first_row)

all_results = result.fetchall()
print(all_results)

many_rows = result.fetchmany(10)
print(many_rows)