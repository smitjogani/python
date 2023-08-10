import mysql.connector as mydb
db_name = input("Enter database name : ")

try:
    pydb = mydb.connect(
        host="localhost",
        username="root",
        passwd=""
    )
except:
    print("There are problem to connecting mysql server")

try:
    pycursor = pydb.cursor()
    pycursor.execute("create database %s"%db_name)
    pycursor.close()
except:
    print("Database already created")
else:
    print("databse successfully created")