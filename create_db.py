import sqlite3 as sql

#connect to SQLite
con = sql.connect('BD1.db')
print("Database opened successfully") 

#Create a Connection
cur = con.cursor()

#Drop users table if already exsist.
cur.execute("DROP TABLE IF EXISTS clientes")

#Create users table  in db_web database

cur.execute("create table clientes (UID TEXT PRIMARY KEY, UNAME TEXT, CONTACT TEXT ) ")
print("Table created successfully")  
#commit changes
con.commit()

#close the connection
con.close()

