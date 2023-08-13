from tkinter import *
import tkinter as tk
from tkinter import messagebox
import mysql.connector
from prettytable import PrettyTable

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="chonlatis"
)
mycursor = mydb.cursor()

window = Tk()
window.title("ตารางส่วนผสม")
window.geometry("500x700")

Label(window, text="", font="14").grid(row=0, column=1)
#ID
Label(window, text="ID").grid(row=1, column=0)
Id = Entry(window)
Id.grid(row=1, column=1)
#ชื่อสูตร
Label(window, text="ชื่อสูตร").grid(row=2, column=0)
Recipename = Entry(window)
Recipename.grid(row=2, column=1)
#ชื่อผู้คิดค้น
Label(window, text="ชื่อผู้คิดค้น").grid(row=3, column=0)
InventorIsName = Entry(window)
InventorIsName.grid(row=3, column=1)
#ส่วนผสม/ปริมาณ
Label(window, text="ส่วนผสม 1").grid(row=4, column=0)
Ingredient1 = Entry(window)
Ingredient1.grid(row=4, column=1)
Label(window, text="ปริมาณ1").grid(row=4, column=3)
Amount1 = Entry(window)
Amount1.grid(row=4, column=4)
Label(window, text="ส่วนผสม 2").grid(row=5, column=0)
Ingredient2 = Entry(window)
Ingredient2.grid(row=5, column=1)
Label(window, text="ปริมาณ2").grid(row=5, column=3)
Amount2 = Entry(window)
Amount2.grid(row=5, column=4)
Label(window, text="ส่วนผสม 3").grid(row=6, column=0)
Ingredient3 = Entry(window)
Ingredient3.grid(row=6, column=1)
Label(window, text="ปริมาณ3").grid(row=6, column=3)
Amount3 = Entry(window)
Amount3.grid(row=6, column=4)
Label(window, text="ส่วนผสม 4").grid(row=7, column=0)
Ingredient4 = Entry(window)
Ingredient4.grid(row=7, column=1)
Label(window, text="ปริมาณ4").grid(row=7, column=3)
Amount4 = Entry(window)
Amount4.grid(row=7, column=4)
Label(window, text="ส่วนผสม 5").grid(row=8, column=0)
Ingredient5 = Entry(window)
Ingredient5.grid(row=8, column=1)
Label(window, text="ปริมาณ5").grid(row=8, column=3)
Amount5 = Entry(window)
Amount5.grid(row=8, column=4)
Label(window, text="ส่วนผสม 6").grid(row=9, column=0)
Ingredient6 = Entry(window)
Ingredient6.grid(row=9, column=1)
Label(window, text="ปริมาณ6").grid(row=9, column=3)
Amount6 = Entry(window)
Amount6.grid(row=9, column=4)
Label(window, text="ส่วนผสม 7").grid(row=10, column=0)
Ingredient7 = Entry(window)
Ingredient7.grid(row=10, column=1)
Label(window, text="ปริมาณ7").grid(row=10, column=3)
Amount7 = Entry(window)
Amount7.grid(row=10, column=4)
Label(window, text="ส่วนผสม 8").grid(row=11, column=0)
Ingredient8 = Entry(window)
Ingredient8.grid(row=11, column=1)
Label(window, text="ปริมาณ8").grid(row=11, column=3)
Amount8 = Entry(window)
Amount8.grid(row=11, column=4)
Label(window, text="ส่วนผสม 9").grid(row=12, column=0)
Ingredient9 = Entry(window)
Ingredient9.grid(row=12, column=1)
Label(window, text="ปริมาณ9").grid(row=12, column=3)
Amount9 = Entry(window)
Amount9.grid(row=12, column=4)
Label(window, text="ส่วนผสม 10").grid(row=13, column=0)
Ingredient10 = Entry(window)
Ingredient10.grid(row=13, column=1)
Label(window, text="ปริมาณ10").grid(row=13, column=3)
Amount10 = Entry(window)
Amount10.grid(row=13, column=4)
#Register
def register():
    sql = "INSERT INTO chonlatis01 (Recipename, InventorIsName, Ingredient1, Amount1, Ingredient2, Amount2, Ingredient3, Amount3, Ingredient4, Amount4, Ingredient5, Amount5, Ingredient6, Amount6, Ingredient7, Amount7, Ingredient8, Amount8, Ingredient9, Amount9, Ingredient10, Amount10) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    if(Recipename.get() != "" and InventorIsName.get() != ""):
        val = (Recipename.get(), InventorIsName.get(), Ingredient1.get(), Amount1.get(), Ingredient2.get(), Amount2.get(), Ingredient3.get(), Amount3.get(), Ingredient4.get(), Amount4.get(), Ingredient5.get(), Amount5.get(), Ingredient6.get(), Amount6.get(), Ingredient7.get(), Amount7.get(), Ingredient8.get(), Amount8.get(), Ingredient9.get(), Amount9.get(), Ingredient10.get(), Amount10.get())
        mycursor.execute(sql, val)
        mydb.commit()
        messagebox.showinfo("Alert","New entry inserted")
        printTable()
    else:
        messagebox.showinfo("Alert","Please fill all entries!")









#Button
Button(window, text="Register", command=register).grid(row=14, column=0)

"""
def printTable():
#ตารางที่จะแสดงผลใน text 
    t = Text(window, height=10, width=50)
    x = PrettyTable() #https://pypi.org/project/prettytable/
    x.field_names = ["Id", "ชื่อสูตร", "ชื่อผู้คิดค้น", "ส่วนผสม 1", "ปริมาณ1", "ส่วนผสม 2", "ปริมาณ2", "ส่วนผสม 3", "ปริมาณ3", "ส่วนผสม 4", "ปริมาณ4", "ส่วนผสม 5", "ปริมาณ5", "ส่วนผสม 6", "ปริมาณ6", "ส่วนผสม 7", "ปริมาณ7", "ส่วนผสม 8", "ปริมาณ8", "ส่วนผสม 9", "ปริมาณ9", "ส่วนผสม 10", "ปริมาณ10"]
    #เพิ่มข้อมูล add row
    sql = "SELECT * FROM chonlatis01"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    for i in result:
        x.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11], i[12], i[13], i[14], i[15], i[16], i[17], i[18], i[19], i[20], i[21], i[22], i[23]])
    #end rows
    t.insert(INSERT, x)
    t.grid(row=15, column=0, columnspan=3)
printTable()
"""
window.mainloop()