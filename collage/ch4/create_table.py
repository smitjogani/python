import mysql.connector

mydb = mysql.connector.connect(host="localhost",username="root",passwd="",database="demo1")
cursor = mydb.cursor()
std_id = int(input("Enter the id : "))
std_name = input("Enter the name : ")

try:
    # cursor.execute("create table student(id int primary key,name varchar(30))") #create table
    cursor.execute("insert into student values('%d','%s')"%(std_id,std_name)) #insert value
    mydb.commit()
    print("Table created")
except:
    print("Error!!")