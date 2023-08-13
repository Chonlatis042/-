month=("January","February","March","April","May","June","July","August","September","October","November","0December")
DAY,MONTH,YEAR,NEXTDATE = 0,0,0,0
###############################################(label)###################################################
from tkinter import*
from tkinter import ttk
import tkinter as tk
root = Tk()
root.title("Nextdate"),root.geometry("300x200")
Label(text="DAY",font=30).grid(row=1,column=1),Label(text="YEAR",font=30).grid(row=3,column=1),Label(text="NEXTDATE",font=30).grid(row=4,column=1)
LB1=Entry(root)
LB2=Entry(root) 
LB3=Entry(root)
LB4=Entry(root)
LB1.grid(row=1,column=2),LB2.grid(row=2,column=2),LB3.grid(row=3,column=2),LB4.grid(row=4,column=2)
CM = StringVar(value="เลือกเดือน")
Label(text="MONTH",font=30).grid(row=2,column=1)
combo=ttk.Combobox(width=15,font=30,textvariable=CM)
combo["values"] = month
combo.grid(row=2,column=2)
##########################################(การคำนวน)##################################################
def NetDate():
    DDAY=int(LB1.get())
    MMONTH=CM.get()
    YYEAR=int(LB3.get())
    if YYEAR >1900 and YYEAR <= 2022:
        if MMONTH == month[1]:
            if DDAY >=1 and DDAY <=28: 
               DDAY = DDAY + 1
               NexD=(DDAY,MMONTH,YYEAR)
               LB4.insert(0,NexD)
            elif DDAY ==29:
                DDAY=1
                MMONTH = month[2]
                NexD=(DDAY,MMONTH,YYEAR)
                LB4.insert(0,NexD)
        else :
            print(0,"Error")
def NetDate2():
    if YYEAR >1900 and YYEAR <= 2022:
        if MMONTH == month[0]:
            if DDAY >=1 and DDAY <= 31:
                DDAY = DDAY + 1
                NexD2=(DDAY,MMONTH,YYEAR) 
                LB4.insert(0,NexD2)
            elif DDAY ==31:
                DDAY=1
                MMONTH = month[1]
                NexD2=(DDAY,MMONTH,YYEAR)
                LB4.insert(0,NexD2)

            
                
                    

            



            
        








Button(text="k",font=30,command=NetDate).grid(row=7,column=1)
root.mainloop()