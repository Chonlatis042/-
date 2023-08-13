from tkinter import *
import tkinter as tk
from tkinter import messagebox
# สร้างหน้าต่าง
window = Tk()
window.title("โปรแกรมคำนวนค่าเหนื่อย")
window.geometry("300x200")
#ใส่สีพื้นหลัง
frame = Frame(window)
frame.config(background="silver")
frame.place(width=300, height=200)
#ข้อความ
Label(window, bg="gold", text="คุณทำได้เท่าไร", font="20", fg="red").grid(row=1, column=1)
####ช่องใส่เลขจำนวนทั้ง3
  #Locks
Label(window, text="Locks").grid(row=2, column=0)
Locks = Entry(window)
Locks.grid(row=2, column=1,columnspan=4)
  #Stocks
Label(window, text="Stocks").grid(row=3, column=0)
Stocks = Entry(window)
Stocks.grid(row=3, column=1,columnspan=4)
  #Barrels
Label(window, text="Barrels").grid(row=4, column=0)
Barrels= Entry(window)
Barrels.grid(row=4, column=1,columnspan=4)
#ปุ่ม
test = Button(window,text='เริ่มทำงานได้', command= lambda:Commiss()).grid(row=5,column=1)
# การคำนวน และ การตรวจค่า
def Commiss():
    locks = int(Locks.get())
    stocks = int(Stocks.get())
    barrels = int(Barrels.get())
    #หาCommissionไม่ได้
    if locks > 70: 
        messagebox.showerror("ใส่ไม่ถูก","กรุณาใส่ไห้ถูก\nต้องใส่น้อยกว่า70")
        result_label = tk.Label(window, text=f'ค่าLocksเกินก่วา70', font=('Tahoma Bold', 10), fg="red")
        result_label.grid(row=6,column=0,columnspan=4)
    elif locks < 1:
        messagebox.showerror("ใส่ไม่ถูก","กรุณาใส่ไห้ถูก\nใส่น้อยกว่า1ไม่ได้")
        result_label = tk.Label(window, text=f'ค่าLocksน้อยกว่า1', font=('Tahoma Bold', 10), fg="red")
        result_label.grid(row=6,column=0,columnspan=4)
    elif stocks > 80:
        messagebox.showerror("ใส่ไม่ถูก","กรุณาใส่ไห้ถูก\nต้องใส่น้อยกว่า80")
        result_label = tk.Label(window, text=f'ค่าStocksเกินก่วา80', font=('Tahoma Bold', 10), fg="red")
        result_label.grid(row=6,column=0,columnspan=4)
    elif stocks < 1:
        messagebox.showerror("ใส่ไม่ถูก","กรุณาใส่ไห้ถูก\nใส่น้อยกว่า1ไม่ได้")
        result_label = tk.Label(window, text=f'ค่าStocksน้อยกว่า1', font=('Tahoma Bold', 10), fg="red")
        result_label.grid(row=6,column=0,columnspan=4)
    elif barrels > 90:
        messagebox.showerror("ใส่ไม่ถูก","กรุณาใส่ไห้ถูก\nต้องใส่น้อยกว่า90")
        result_label = tk.Label(window, text=f'ค่าBarrelsเกินก่วา90', font=('Tahoma Bold', 10), fg="red")
        result_label.grid(row=6,column=0,columnspan=4)
    elif barrels < 1:
        messagebox.showerror("ใส่ไม่ถูก","กรุณาใส่ไห้ถูก\nใส่น้อยกว่า1ไม่ได้")
        result_label = tk.Label(window, text=f'ค่าBarrelsน้อยกว่า1', font=('Tahoma Bold', 10), fg="red")
        result_label.grid(row=6,column=0,columnspan=4)
    else :
        sales = 45 * locks + 30 * stocks + 25 * barrels
        commission = 0

        if sales <= 1000:
            commission = sales * 0.1
            result_label = tk.Label(window, text=f'sales ที่ได้ : {sales}', font=('Tahoma Bold', 10), fg="red", bg="silver")
            result_label.grid(row=6,column=0,columnspan=4)
        elif sales <= 1800:
            commission = 1000 * 0.1 + (sales - 1000) * 0.15
            result_label = tk.Label(window, text=f'sales ที่ได้ : {sales}', font=('Tahoma Bold', 10), fg="red", bg="silver")
            result_label.grid(row=6,column=0,columnspan=4)
        else:
            commission = 1000 * 0.1 + 800 * 0.15 + (sales - 1800) * 0.2
            result_label = tk.Label(window, text=f'sales ที่ได้ : {sales}', font=('Tahoma Bold', 10), fg="red", bg="silver")
            result_label.grid(row=6,column=0,columnspan=4)
    result_label = tk.Label(window, text=f'Commission ที่ได้ : {commission}', font=('Tahoma Bold', 10), fg="#0000FF", bg="silver")
    result_label.grid(row=7,column=0,columnspan=4)
window.mainloop()