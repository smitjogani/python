import mysql.connector

mydb = mysql.connector.connect(host="localhost",username="root",passwd="")
cursor = mydb.cursor()
try:
    cursor.execute("create database demo1")
    mydb.commit()
    print("Database created")
except:
    print("Error!!")