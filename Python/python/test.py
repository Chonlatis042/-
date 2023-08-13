from tkinter import *
import tkinter as tk
from tkinter import messagebox
window = Tk()
window.title("Program Next Date")
window.geometry("300x200")
Label(window, bg="gold", text="Next Date", font="20", fg="red").grid(row=1, column=1)
Label(window, text="month").grid(row=2, column=0)
Months = Entry(window)
Months.grid(row=2, column=1)
Label(window, text="day").grid(row=3, column=0)
Days = Entry(window)
Days.grid(row=3, column=1)
Label(window, text="year").grid(row=4, column=0)
Years = Entry(window)
Years.grid(row=4, column=1)
Label(window, text="").grid(row=5, column=1)
result = Label(window)
result.grid(row=6, column=1)
Label(window, text="").grid(row=7, column=1)
OK = Button(window, text='OK', command= lambda: display()).grid(row=2, column=4, sticky=(W,E))
def clear_button():
    Months.delete(0, END)
    Days.delete(0, END)
    Years.delete(0, END)
def leap_year(year):
    return ( (year%400 == 0) or ( (year%100 !=0) and (year%4 ==0)) )
def last_day(month, year):
    months_31_days = ['January', 'March', 'May', 'July', 'August', 'October', 'December']
    if month == 'February':
        if leap_year(year):
            return 29
        else:
            return 28
    elif month in months_31_days:
        return 31
    else:
        return 30
def nextDate(month,day,year):
    if day== 31 and month == "December":
        month = 'January'
        day = 1
        year = year + 1
    elif day == last_day(month,year):
        if month == "December":
            month = 'January'
            year = year + 1
        else:
            month_index = ["January","February","March","April","May","June","July","August","September","October","November","December"].index(month)
            month = ["January","February","March","April","May","June","July","August","September","October","November","December"][month_index + 1]
        day = 1     
    elif day >= 1 and day < last_day(month,year):
        day = day + 1
    return [str(month),int(day),int(year)]
def display():
    try:
        month = str(Months.get())
        day = int(Days.get())
        year = int(Years.get())
        
        if month.isdigit():
            messagebox.showerror("Error!", "Invalid input. Ensure month as name month")
        elif month not in ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]:
            messagebox.showerror("Error!", "ใส่เดือนผิด")
        elif (day < 1 or day > 31):
            messagebox.showerror("Error!", "Invalid input. Ensure day between 1-31")
        elif (year < 1812 or year > 2012):
            messagebox.showerror("Error!", "Invalid input. Ensure year for 1812-2012")
        else:
            date = nextDate(month, day, year)
            result.config(text=f"{date[0]} {date[1]} {date[2]}")
    except ValueError:
        messagebox.showerror("Error!", "Please enter the month as a string, the date as an integer and the year from 1812-2012.")
Cancle = Button(window, text='Clear', command=clear_button).grid(row=3, column=4, sticky=(W,E))
window.mainloop()