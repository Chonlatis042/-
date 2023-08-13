from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
from prettytable import PrettyTable
### Connect DB ###
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="111"
)
mycursor = mydb.cursor()



window = Tk()
window.title("Student's information")
window.geometry("500x400")

Label(window, text="Final LAB", font="14").grid(row=0, column=1)
#Product_ID
Label(window, text="Product_ID").grid(row=2, column=0)
product_ID = Entry(window)
product_ID.grid(row=2, column=1)
#Product_Name 
Label(window, text="Product_Name").grid(row=3, column=0)
product_Name = Entry(window)
product_Name.grid(row=3, column=1)
#UnitPrice 
Label(window, text="UnitPrice ").grid(row=4, column=0)
unitPrice  = Entry(window)
unitPrice .grid(row=4, column=1)
#Stock 
Label(window, text="Stock").grid(row=5, column=0)
stock  = Entry(window)
stock .grid(row=5, column=1)
#Register
def register():
    sql = "INSERT INTO Products (Product_ID, Product_Name, UnitPrice, Stock ) VALUES (%s, %s, %s, %s)"

    if(product_ID.get() != "" and product_Name.get() != ""):
        
        val = (product_ID.get(), product_Name.get(), unitPrice.get(), stock.get())
        mycursor.execute(sql, val)
        mydb.commit()
        messagebox.showinfo("Alert","New entry inserted")
        showData()
    else:
        messagebox.showinfo("Alert","Please fill all entries!")
#Search
def search():
    product_Name.delete(0, 'end')
    unitPrice.delete(0, 'end')
    stock.delete(0, 'end')

    sql = "SELECT * FROM Products WHERE Product_ID = '%d'" %(int(product_ID.get()))
    mycursor.execute(sql)
    result = mycursor.fetchone()
    
    product_ID.set(result[1])
    product_Name.insert(0, result[2])
    unitPrice.insert(0, result[3])
    stock.insert(0, result[4])

def update():
    sql = "UPDATE Products SET  product_Name = '%s', unitPrice = '%s', stock = '%s' WHERE product_ID = '%d'" %( product_Name.get(), unitPrice.get(), stock.get(), int(product_ID.get()))
    mycursor.execute(sql)
    mydb.commit()
    messagebox.showinfo("Alert","Record updated!")
    showData()

def delete():
    sql = "DELETE FROM Products WHERE id = '%d'" %(int(product_ID.get()))
    mycursor.execute(sql)
    mydb.commit()
    messagebox.showinfo("Alert","Record deleted!")
    showData()
   
def clearText():
    product_ID.delete(0, 'end')
    product_Name.delete(0, 'end')
    unitPrice.delete(0, 'end')
    stock.delete(0, 'end')
    #Button
Button(window, text="Register", command=register).grid(row=2, column=2)
Button(window, text="Search", command=search).grid(row=3, column=2)
Button(window, text="Update", command=update).grid(row=4, column=2)
Button(window, text="Delete", command=delete).grid(row=5, column=2)


def showData():
    # define columns
    columns = ('orderDetail_ID', 'order_ID', 'product_ID', 'amount')
    tree = ttk.Treeview(window, columns=columns, show='headings')

    # define headings
    tree.heading('orderDetail_ID', text='OrderDetail_ID')
    tree.column("orderDetail_ID", minwidth=0, width=50, stretch=NO)
    tree.heading('order_ID', text='Order_ID')
    tree.column("order_ID", minwidth=0, width=50, stretch=NO)
    tree.heading('product_ID', text='Product_ID')
    tree.column("product_ID", minwidth=0, width=120, stretch=NO)
    tree.heading('amount', text='Amount')
    tree.column("amount", minwidth=0, width=120, stretch=NO)
    #tree.heading('tel', text='Tel')
    #tree.column("tel", minwidth=0, width=100, stretch=NO)

    #Add rows
    sql = "SELECT * FROM OrderDetails"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    for i in result:
        tree.insert('', tk.END, values=i)
    #End rows

    def item_selected(event):
        for selected_item in tree.selection():
            item = tree.item(selected_item)
            record = item['values']

            # clear text before insert to entry
            clearText()

            # insert data to entry
            orderDetail_ID.insert(0,record[0])
            order_ID.set(record[1])
            product_ID.insert(0,record[2])
            amount.insert(0,record[3])
            #tel.insert(0,record[4])
    
    tree.bind('<<TreeviewSelect>>', item_selected)
    
    tree.grid(row=6, column=0, columnspan=3, padx=10, sticky='nsew')

showData()




window.mainloop()