#------------------------------------------------------(ตัวเเปร)-----------------------------------------------------------------------
lockPrice,stockPrice,barrelPrice,locks,stocks,barrels,commission  = 45.0,30.0,25.0,0,0,0,0.0
#------------------------------------------------------(GUI)-------------------------------------------------------------------------
from tkinter import*
import tkinter as tk
root = Tk()
root.title("comision"),root.geometry("300x200")
#------------------------------------------------------(GUI label)-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Label(text="Locks",font=30).grid(row=2,sticky=W),Label(text="Stocks",font=30).grid(row=3,sticky=W),Label(text="Barrels",font=30).grid(row=4,sticky=W),Label(text="sale",font=30).grid(row=5,sticky=W),Label(text="Result",font=30).grid(row=6,sticky=W)
#------------------------------------------------------(ช่องข้อมูลเเต่ละช่อง)-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
et1=Entry(root)#lock
et2=Entry(root)#stock
et3=Entry(root)#barrel
et4=Entry(root)#sale
et5=Entry(root)#commisson
et1.grid(row=2,column=1),et2.grid(row=3,column=1),et3.grid(row=4,column=1),et4.grid(row=5,column=1),et5.grid(row=6,column=1)
#------------------------------------------------------(Calculator)------------------------------------------------------------------
def calcurator():
    locks=int(et1.get()) #get จะไปดึง et1=locks
    if (locks >=1 and locks <=70):
        stocks=int(et2.get())
        lok=locks*lockPrice
        if (stocks >=1 and stocks <=80):
            barrels=int(et3.get())
            sto=stocks*stockPrice
            if (barrels >=1 and barrels <=90):
                barr=barrels*barrelPrice
                sale=lok+sto+barr
                commission = str(calcurator2(sale)) #สร้างตัวเเปลเก็บค่าคอมเพื่อเก็บค่าที่เรียกใช้ํฟังชั่นมา
                et4.insert(0,sale)
                et5.insert(0,commission)
            else :
                et5.insert(0,"Error")
        else :
            et5.insert(0,"Error")
    else :
        et5.insert(0,"Error")
def calcurator2(sale):
    if (sale > 1800.0):
        commission = 0.10 * 1000.0  
        commission = commission + 0.15 * 800.0
        commission = commission + 0.20 * (sale - 1800.0)
        return commission
    elif (sale > 1000.0):
        commission = 0.10 * 1000.0
        commission = commission + 0.15 * (sale - 1000.0)
        return commission
    else:
        commission = 0.10 * sale
        return commission
def clear():
    et1.delete(0,"end"),et2.delete(0,"end"),et3.delete(0,"end"),et4.delete(0,"end"),et5.delete(0,"end")
#------------------------------------------------------(Button)----------------------------------------------------------------------
Button(text="คิด",font=30,command=calcurator).grid(row=7,column=1),Button(text="ล้าง",font=30,command=clear).grid(row=7,column=2)
root.mainloop()
#------------------------------------------------------------------------------------------------------------------------------------
