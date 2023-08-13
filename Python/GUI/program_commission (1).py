from tkinter import*
from tkinter import ttk
month=("January","February","March","April","May","June","July","August","September","October","November","December")
Nextdate = Tk()
Nextdate.title("Nextdate"),Nextdate.geometry("400x200")
month=("January","February","March","April","May","June","July","August","September","October","November","December")
Label(text="DAY",font=30).grid(row=1,column=1),Label(text="YEAR",font=30).grid(row=3,column=1),Label(text="NEXTDATE",font=30).grid(row=4,column=1)
LB1=Entry(Nextdate)
LB2=Entry(Nextdate) 
LB3=Entry(Nextdate)
LB4=Entry(Nextdate)
LB1.grid(row=1,column=2),LB2.grid(row=2,column=2),LB3.grid(row=3,column=2),LB4.grid(row=4,column=2)
CM = StringVar(value="choose")
Label(text="MONTH",font=30).grid(row=2,column=1)
combo=ttk.Combobox(width=15,font=30,textvariable=CM)
combo["values"] = month
combo.grid(row=2,column=2)
def NetDate():
    DDAY=int(LB1.get())
    MMONTH=combo.get()
    YYEAR=int(LB3.get())
    LB4.delete(0,"end")
    if YYEAR >1812 and YYEAR <= 2022:
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
                LB4.insert(0,"Error")
        elif MMONTH == month[0] or MMONTH == month[2] or MMONTH == month[4] or MMONTH == month[6] or MMONTH == month[7] or MMONTH == month[9] or MMONTH == month[11]:
            if DDAY >=1 and DDAY < 31:
                DDAY = DDAY + 1
                NexD2=(DDAY,MMONTH,YYEAR) 
                LB4.insert(0,NexD2)
            elif DDAY ==31:
                DDAY=1
                MMONTH = month[1]
                NexD2=(DDAY,MMONTH,YYEAR)
                LB4.insert(0,NexD2)
            else :
                LB4.insert(0,"Error")
    elif MMONTH == month[3] or MMONTH == month[5] or MMONTH == month[8] or MMONTH == month[10]:
        if DDAY >=1 and DDAY < 30:
            DDAY = DDAY + 1
            NexD2=(DDAY,MMONTH,YYEAR) 
            LB4.insert(0,NexD2)
        elif DDAY ==30:
            DDAY=1
            MMONTH = month[1]
            NexD2=(DDAY,MMONTH,YYEAR)
            LB4.insert(0,NexD2)
        else :
            LB4.insert(0,"Error")
Button(text="Nextdate",font=30,command=NetDate).grid(row=7,column=1)
Nextdate.mainloop()