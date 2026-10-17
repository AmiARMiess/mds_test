import pandas as pd
# import mysql.connector
from sqlalchemy import create_engine

# Connect to the sakila database using SQLAlchemy (recommended for pandas)
# engine = create_engine('mysql+pymysql://mdsGlobalUser:mds$uper$ecurePassword123@mdsmysql.sci.pitt.edu/sakila')
engine = create_engine('mysql+pymysql://root:@127.0.0.1/hello')

# con = mysql.connector.connect(host='mdsmysql.sci.pitt.edu',
#                              user='mdsGlobalUser',
#                              password='mds$uper$ecurePassword123',
#                              db='sakila')

# conn = mysql.connector.connect(
#     host="127.0.0.1",
#     user="root",
#     password="",
#     database="hello"
# )

query = "SELECT * FROM film;"
films = pd.read_sql(query, engine)
# films.head()

print(films.head())

# query = "SELECT * FROM film WHERE title = %s;"
# params = ('ALIEN CENTER',)
# films = pd.read_sql(query, con=engine, params=params)
# films.head()

# query = "INSERT INTO actor(first_name,last_name,last_update) "
# query += "VALUES (%s,%s,NOW());"

# con.cursor().execute(query, ('Jane', 'Smith')) 
# con.commit()

# query = "UPDATE actor SET first_name = %s WHERE last_name = %s"
# con.cursor().execute(query, ('Jennifer', 'Smith')) 
# con.commit()

# query = "DELETE FROM actor WHERE last_name = %s"
# con.cursor().execute(query, ('Smith',)) 
# con.commit()