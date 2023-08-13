from tkinter import *
from tkinter import messagebox
import customtkinter as cus
from tkinter import ttk
import tkinter as tk

window = tk.Tk()
window.title("Commission")
window.geometry("400x360")
window.configure(bg="grey")

#entry
cus.CTkLabel(window, text="Lock (1-70)", bg_color="gray", text_color="black").place(x=40,y=20)
in_locks = cus.CTkEntry(window, width=150, border_color="gray")
in_locks.place(x=130,y=20)

cus.CTkLabel(window, text="Stock (1-80)", bg_color="gray", text_color="black").place(x=40,y=50)
in_stocks = cus.CTkEntry(window, width=150, border_color="gray")
in_stocks.place(x=130,y=50)

cus.CTkLabel(window, text="Barrel (1-90)", bg_color="gray", text_color="black").place(x=40,y=80)
in_barrels = cus.CTkEntry(window, width=150, border_color="gray")
in_barrels.place(x=130,y=80)

table = ttk.Treeview(window, columns= ("Locks","Stocks","Barrels","Commission"), show ="headings",selectmode="browse")
vsb = ttk.Scrollbar(window, orient="vertical", command=table.yview)
vsb.place(x=165+200+2, y=119, height=226)

table.configure(yscrollcommand=vsb.set)
table.heading("Locks",text= "Locks")
table.column("Locks",width=86,anchor=CENTER)
table.heading("Stocks",text= "Stocks")
table.column("Stocks",width=86,anchor=CENTER)
table.heading("Barrels",text= "Barrels")
table.column("Barrels",width=86,anchor=CENTER)
table.heading("Commission",text= "Commission")
table.column("Commission",width=86,anchor=CENTER)
table.place(x=20,y=120)

#reset to default
def reset():
    for item in table.get_children():
      table.delete(item)
    
#calculate
def cal():       
    try:
        locks=int(in_locks.get())
        stocks=int(in_stocks.get())
        barrels=int(in_barrels.get())
            
        if (type(locks) == int and type(stocks) == int and type(barrels) == int):
            
            if(locks>70 or locks<1):
                messagebox.showwarning("Alert","Number of Lock is out of range")
                
            elif(stocks>80 or stocks<1):
                messagebox.showwarning("Alert","Number of Stock is out of range")
            
            elif(barrels>90 or barrels<1):
                messagebox.showwarning("Alert","Number of Barrel is out of range")
                
            else:
                
                lockSales = 45 * locks
                stockSales = 30 * stocks
                barrelSales = 25 * barrels 
                sale = lockSales + stockSales + barrelSales
                
                if(sale > 1800):
                    commission = 0.1 * 1000
                    commission = commission+(800*0.15)
                    commission = commission+(sale-1800)*0.2
                    
                elif(sale > 1000):
                    commission = 0.1 * 1000
                    commission = commission+(sale-1000)*0.15
                    
                else:
                    commission = 0.1 * sale
                
                #display
                if (commission.is_integer()):
                    result = round(commission)
                    messagebox.showinfo("Result","Lock = %d , Stock = %d , Barrel = %d \n Commission = %d"%(locks,stocks,barrels,result))
                
                else:
                    result = str(commission)
                    messagebox.showinfo("Result","Lock = %d , Stock = %d , Barrel = %d \n Commission = %s"%(locks,stocks,barrels,result))
                
                table.insert(parent = '',index = tk.END ,values = ('%d'%(locks),'%d'%(stocks),'%d'%(barrels),'%s'%(result)))
                
                in_locks.delete(0,END)
                in_stocks.delete(0,END)
                in_barrels.delete(0,END)      
                
    except ValueError :
        
        locks=(in_locks.get())
        stocks=(in_stocks.get())
        barrels=(in_barrels.get())
        
        if (locks == "" or stocks == "" or barrels == ""):   
            messagebox.showwarning("Alert","Not null !!!")
            
        else :
            messagebox.showwarning("Alert","Please enter just integer")
        
        window.destroy()     

#button        
cus.CTkButton(window, text="Calculate",width=80, fg_color="white", hover_color="lightgray", text_color="black",command=cal).place(x=300,y=30)
cus.CTkButton(window, text="Reset",width=80, fg_color="white", hover_color="lightgray", text_color="black",command=reset).place(x=300,y=65)

window.mainloop()