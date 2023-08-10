import mysql.connector as mydb
db_name = input("Enter Database name : ")
tb_name = input("Enter table name :")

def create_table():
    pycursor = mydb.cursor()
    pycursor.execute("create table %s(eid int primary key,name varchar(30),salary int)"%tb_name)
    print("Table created")
    pycursor.close()
    insert_data()

def insert_data():
    n = int(input("Enter w many row you want to add : "))
    for i in range(n):
        pycursor = mydb.cursor()
        eid1 = int(input("Enter Employee Id : "))
        name1 = input("Enter the name : ")
        salary1 = int(input("Enter the Salary : "))
        pycursor.execute(f"insert into {tb_name}(eid,name,salary) values({eid1},{name1},{salary1})")
        mydb.commit()
        print("Row inserted")
        pycursor.close()
        select_data()

def select_data():
    pycursor = mydb.cursor()
    pycursor.executed("select * from %s"%tb_name)
    res = pycursor.fetchall()
    if pycursor.rowcount > 0:
        print(res,"\n")
    else:
        insert_data()

try:
    pydb = mydb.connect(
        host="localhost",
        username="root",
        passwd="",
        database={db_name}
    )
except:
    print("Connection Error")
else:
    try:
        create_table()
    except:
        print("Table Already exists")
        select_data()
    else:
        print("Data insert successfully")