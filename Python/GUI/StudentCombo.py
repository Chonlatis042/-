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
  database="db_python"
)
mycursor = mydb.cursor()
##################

window = Tk()
window.title("Final LAB")
window.geometry("500x400")

#sid = tk.IntVar()
#fname = tk.StringVar()
#lname = tk.StringVar()
#tele = tk.StringVar()

Label(window, text="Final LAB", font="14").grid(row=0, column=1)

#ID
Label(window, text="ID").grid(row=1, column=0)
id = Entry(window)
id.grid(row=1, column=1)

#Title
Label(window, text="Title").grid(row=2, column=0)

# create a combobox to get all title
sql = "SELECT title FROM student"
mycursor.execute(sql)
results = mycursor.fetchall()
results_for_combobox = [result[0] for result in results]
title_cb = ttk.Combobox(window,values=results_for_combobox)

# prevent typing a value
title_cb['state'] = 'readonly'

title_cb.grid(row=2, column=1)

#Firstname
Label(window, text="First name").grid(row=3, column=0)
firstname = Entry(window)
firstname.grid(row=3, column=1)

#Lastname
Label(window, text="Last name").grid(row=4, column=0)
lastname = Entry(window)
lastname.grid(row=4, column=1)

#Telephone
Label(window, text="Tel").grid(row=5, column=0)
tel = Entry(window)
tel.grid(row=5, column=1)

#Register
def register():
    sql = "INSERT INTO student (title, firstname, lastname, tel) VALUES (%s, %s, %s, %s)"

    if(firstname.get() != "" and lastname.get() != ""):
        
        val = (title_cb.get(), firstname.get(), lastname.get(), tel.get())
        mycursor.execute(sql, val)
        mydb.commit()
        messagebox.showinfo("Alert","New entry inserted")
        showData()
    else:
        messagebox.showinfo("Alert","Please fill all entries!")

#Search
def search():
    firstname.delete(0, 'end')
    lastname.delete(0, 'end')
    tel.delete(0, 'end')

    sql = "SELECT * FROM student WHERE id = '%d'" %(int(id.get()))
    mycursor.execute(sql)
    result = mycursor.fetchone()
    
    title_cb.set(result[1])
    firstname.insert(0, result[2])
    lastname.insert(0, result[3])
    tel.insert(0, result[4])

def update():
    sql = "UPDATE student SET title='%s', firstname = '%s', lastname = '%s', tel = '%s' WHERE id = '%d'" %(title_cb.get(), firstname.get(), lastname.get(), tel.get(), int(id.get()))
    mycursor.execute(sql)
    mydb.commit()
    messagebox.showinfo("Alert","Record updated!")
    showData()

def delete():
    sql = "DELETE FROM student WHERE id = '%d'" %(int(id.get()))
    mycursor.execute(sql)
    mydb.commit()
    messagebox.showinfo("Alert","Record deleted!")
    showData()
   
def clearText():
    id.delete(0, 'end')
    title_cb.set('')
    firstname.delete(0, 'end')
    lastname.delete(0, 'end')
    tel.delete(0, 'end')

#Button
Button(window, text="Register", command=register).grid(row=1, column=2)
Button(window, text="Search", command=search).grid(row=2, column=2)
Button(window, text="Update", command=update).grid(row=3, column=2)
Button(window, text="Delete", command=delete).grid(row=4, column=2)

def showData():
    # define columns
    columns = ('id', 'title', 'first_name', 'last_name', 'tel')
    tree = ttk.Treeview(window, columns=columns, show='headings')

    # define headings
    tree.heading('id', text='ID')
    tree.column("id", minwidth=0, width=50, stretch=NO)
    tree.heading('title', text='Title')
    tree.column("title", minwidth=0, width=50, stretch=NO)
    tree.heading('first_name', text='First Name')
    tree.column("first_name", minwidth=0, width=120, stretch=NO)
    tree.heading('last_name', text='Last Name')
    tree.column("last_name", minwidth=0, width=120, stretch=NO)
    tree.heading('tel', text='Tel')
    tree.column("tel", minwidth=0, width=100, stretch=NO)

    #Add rows
    sql = "SELECT * FROM student"
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
            id.insert(0,record[0])
            title_cb.set(record[1])
            firstname.insert(0,record[2])
            lastname.insert(0,record[3])
            tel.insert(0,record[4])
    
    tree.bind('<<TreeviewSelect>>', item_selected)
    
    tree.grid(row=6, column=0, columnspan=3, padx=10, sticky='nsew')

showData()

window.mainloop()