
from tkinter import*
import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("โปรแกรมคำนวณค่าคอมมิชชั่น")
window.geometry("700x100")

tk.Label(text="lock", font=(15)).grid(row=1,column=0)
locks_entry = tk.Entry(window)
locks_entry.grid(row=1,column=1)

tk.Label(text="stock", font=(15)).grid(row=1,column=2)
stocks_entry = tk.Entry(window)
stocks_entry.grid(row=1,column=3)

tk.Label(text="barrel", font=(15)).grid(row=1,column=4)
barrels_entry = tk.Entry(window)
barrels_entry.grid(row=1,column=5)

run = tk.Button(window, text="ตรวจสอบ", font=(15),command=lambda: results())
run.grid(row=2,column=3)

output = Label(window)
output.grid(row=3,column=3)

def results():
    try :
       lock = int(locks_entry.get())
       stock = int(stocks_entry.get())
       barrel = int(barrels_entry.get())
       
       sales = 45 * lock + 30 * stock + 25 * barrel

       if sales <= 1000:
        commission = sales * 0.10
       elif sales <= 1800: 
        commission = 1000 * 0.10 + (sales - 1000) * 0.15
       else:
        commission = 1000 * 0.10 + 800 * 0.15 + (sales - 1800) * 0.20
        
       if lock > 70:
        messagebox.showinfo("Error","ใส่ตัวเลขระหว่าง 1-70")
       elif lock < 1:
        messagebox.showinfo("Error","ใส่ตัวเลขระหว่าง 1-70")
       if stock > 80:
        messagebox.showinfo("Error","ใส่ตัวเลขระหว่าง 1-80")
       elif stock < 1:
        messagebox.showinfo("Error","ใส่ตัวเลขระหว่าง 1-80")
       if barrel > 90:
        messagebox.showinfo("Error","ใส่ตัวเลขระหว่าง 1-90")
       elif barrel < 1:
        messagebox.showinfo("Error","ใส่ตัวเลขระหว่าง 1-90")
        
    except ValueError: messagebox.showerror("Error","โปรดใส่ข้อมูลเป็นตัวเลขเท่านั้น!!")
    output.config(text="คุณได้ค่าคอมมิชชั่น $" + str(commission))

window.mainloop()