from tkinter import *
from tkinter import messagebox
import tkinter as tk

window = Tk()
window.title("Login")
window.geometry("500x300")

frame = Frame(window)
frame.config(background="silver")
frame.place(width=500, height=300, x=0, y=0)

Label(window, bg="gold", text="Login ID").pack(ipadx=5, ipady=5)
txt_input = tk.StringVar()
Entry(window, textvariable=txt_input).pack()


def chkLogin():
    msg = "Your input is " + tat_ipput.get()
    messagebox.showinfo("แจ้วเตือน",message=msg)

btn = Button(window, command=chkLogin, text="บันทึก", width=5, height=2)
btn.pack(padx=5, pady=10) # expand=True

window.mainloop()