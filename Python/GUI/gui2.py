from tkinter import*
import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Commission Program")
window.geometry("500x250")

tk.Label(window, text="Commission", font=('Arial Bold', 15), fg="#FF0000").grid(row=0, column=1)

tk.Label(text="locks", font=('Arial Bold', 15), fg="purple").grid(row=1,column=0)
locks_entry = tk.Entry(window)
locks_entry.grid(row=1,column=2)

tk.Label(text="stocks", font=('Arial Bold', 15), fg="orange").grid(row=2,column=0)
stocks_entry = tk.Entry(window)
stocks_entry.grid(row=2,column=2)

tk.Label(text="barrels", font=('Arial Bold', 15), fg="#FFA07A").grid(row=3,column=0)
barrels_entry = tk.Entry(window)
barrels_entry.grid(row=3,column=2)

Cancle = tk.Button(window, text='Cancel', bg='yellow', fg="#0000FF", command= lambda: clear_button())
Cancle.grid(row=3, column=3, sticky=(W,E),  padx=(20,5), pady=(5,20))
Cancle.config(font=('Tahoma Bold', 12), width=10)


def clear_button():
    locks_entry.delete(0, END)
    stocks_entry.delete(0, END)
    barrels_entry.delete(0, END)

def calculate_commission():
    try :
       locks = int(locks_entry.get())
       stocks = int(stocks_entry.get())
       barrels = int(barrels_entry.get())

       sales = 45 * locks + 30 * stocks + 25 * barrels
       commission = 0

       if sales <= 1000:
        commission = sales * 0.1
       elif sales <= 1800:
        commission = 1000 * 0.1 + (sales - 1000) * 0.15
       else:
        commission = 1000 * 0.1 + 800 * 0.15 + (sales - 1800) * 0.2

       if locks > 70:
        messagebox.showerror("Error","Error: You entered an invalid amount. Please enter the number of locks between 1-70.")
       elif locks < 1:
        messagebox.showerror("Error","Error: You entered an invalid amount. Please enter the number of locks between 1-70.")
       if stocks > 80:
        messagebox.showerror("Error","Error: You entered an invalid amount. Please enter the number of stocks between 1-80.")
       elif stocks < 1:
        messagebox.showerror("Error","Error: You entered an invalid amount. Please enter the number of stocks between 1-80.")
       if barrels > 90:
        messagebox.showerror("Error","Error: You entered an invalid amount. Please enter the number of barrels between 1-90.")
       elif barrels < 1:
        messagebox.showerror("Error","Error: You entered an invalid amount. Please enter the number of barrels between 1-90.")
    except ValueError: messagebox.showerror("Error","Error: Please enter the number type integer")
    result_label = tk.Label(window, text=f'Commission for {locks} locks {stocks} stocks {barrels} barrels is : ${commission:.2f}', font=('Tahoma Bold', 10), fg="#0000FF")
    result_label.grid(row=6,column=0,columnspan=3)   

CRun = tk.Button(master=window, text="Go", font=('Arial Bold', 15), bg="#7FFF00",command=calculate_commission)
CRun.grid(row=1, column=3, padx=(20,5), pady=(5,20))
CRun.config(font=('Tahoma Bold', 12), width=10)


window.mainloop()