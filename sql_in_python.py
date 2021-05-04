import sqlalchemy

server = 'localhost,1443'
database = 'Northwind'
user = 'SA'
password = 'Passw0rd2018'
driver = '0DCB+Driver+17+for+SQL+server'

engine = sqlalchemy.create_engine(f"mssql+pyodbc://{user}:{password}@{server}/{database}?driver={driver}")
