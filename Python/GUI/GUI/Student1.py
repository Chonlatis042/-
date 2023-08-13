from tkinter import *
import tkinter as tk
from tkinter import messagebox
import mysql.connector
from prettytable import PrettyTable

### Connect DB ###
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="chonlatis"
)
mycursor = mydb.cursor()
##################

window = Tk()
window.title("Student's information")
window.geometry("600x600")

#sid = tk.IntVar()
#fname = tk.StringVar()
#lname = tk.StringVar()
#tele = tk.StringVar()

Label(window, text="Student's information", font="14").grid(row=0, column=1)

#ID
Label(window, text="ID").grid(row=1, column=0)
id = Entry(window)
id.grid(row=1, column=1)

#Firstname
Label(window, text="ชื่อ").grid(row=2, column=0)
firstname = Entry(window)
firstname.grid(row=2, column=1)

#Lastname
Label(window, text="นามสกุล").grid(row=3, column=0)
lastname = Entry(window)
lastname.grid(row=3, column=1)

#Telephone
Label(window, text="เบอร์").grid(row=4, column=0)
tel = Entry(window)
tel.grid(row=4, column=1)

#Register
def register():
    sql = "INSERT INTO students (firstname, lastname, tel) VALUES (%s, %s, %s)"

    if(firstname.get() != "" and lastname.get() != ""):
        val = (firstname.get(), lastname.get(), tel.get())
        mycursor.execute(sql, val)
        mydb.commit()
        messagebox.showinfo("Alert","New entry inserted")
        printTable()
    else:
        messagebox.showinfo("Alert","Please fill all entries!")

#Search
def search():
    # clear text ไม่ให้ข้อมูลซ้ำขณะ search
    firstname.delete(0, 'end')
    lastname.delete(0, 'end')
    tel.delete(0, 'end')

    sql = "SELECT * FROM students WHERE id = '%d'" %(int(id.get()))
    mycursor.execute(sql)
    result = mycursor.fetchall()
    First_Name = ""
    Last_Name = ""
    tel_No = ""
    
    for i in result:
        First_Name = i[1]
        Last_Name = i[2]
        tel_No = i[3]

    firstname.insert(0,First_Name)
    lastname.insert(0,Last_Name)
    tel.insert(0,tel_No)

### Update
def update():
    sql = "UPDATE students SET firstname = '%s', lastname = '%s', tel = '%s' WHERE id = '%d'" %(firstname.get(), lastname.get(), tel.get(), int(id.get()))
    #val = (firstname.get(), lastname.get(), tel.get(), int(id.get()))
    mycursor.execute(sql)
    mydb.commit()
    messagebox.showinfo("Alert","Record updated!")
    printTable()

### Delete
def delete():
    sql = "DELETE FROM students WHERE id = '%d'" %(int(id.get()))
    mycursor.execute(sql)
    mydb.commit()
    messagebox.showinfo("Alert","Record deleted!")
    printTable()
    #ลบเสร็จให้เคลียร์ค่าพวกนี้ทิ้ง
    id.delete(0, 'end')
    firstname.delete(0, 'end')
    lastname.delete(0, 'end')
    tel.delete(0, 'end')

#Button
Button(window, text="Register", command=register).grid(row=1, column=2)
Button(window, text="Search", command=search).grid(row=2, column=2)
Button(window, text="Update", command=update).grid(row=3, column=2)
Button(window, text="Delete", command=delete).grid(row=4, column=2)

def printTable():
#ตารางที่จะแสดงผลใน text 
    t = Text(window, height=10, width=50)
    x = PrettyTable() #https://pypi.org/project/prettytable/
    x.field_names = ["ID", "ชื่อ", "นามสกุล", "เบอร์"]
    #เพิ่มข้อมูล add row
    sql = "SELECT * FROM students"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    for i in result:
        x.add_row([i[0], i[1], i[2], i[3]])
    #end rows
    t.insert(INSERT, x)
    t.grid(row=5, column=0, columnspan=3)
printTable()
window.mainloop()