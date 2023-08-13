from winreg import DeleteKey
import mysql.connector as cn

mydb = cn.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="myDB"
)

mycursor = mydb.cursor()

####DDL
"""
mycursor.execute("create database myDB")
mycursor.execute("create table stndent(stndentID int auto_increment primary key,fistName varchar(50),lastName varchar(50))")
sql="drop table stndents"
mycursor.execute(sql)
print("create DB successfully")
"""
####DML

### insert
"""
sql = "insert into stndent (fistName,lastName) values(%s, %s)"
param = ("ชลทิศ","มิอุบล")
mycursor.execute(sql,param)
mydb.commit()
"""

### delete
mycursor.execute("Delete from stndent where stndentID = 3")
mydb.commit()
print(mycursor.rowcount,"record(s) deleted!\n\n")

### update
sql="update stndent set fistName = %s , lastName = %s where stndentID = 1"
param = ("ชลทิศ","มิอุบล")
mycursor.execute(sql,param)
mydb.commit()

### select
mycursor.execute("select * from stndent")
results = mycursor.fetchall()
for x in results:
    print(x) 
'''
#print("Teansaction successfully")

sql="SELECT * from category inner join product on category.categoryID = product.categoryID "
mycursor.execute(sql)
results = mycursor.fetchall()
for x in results:
    print(x) 
'''





