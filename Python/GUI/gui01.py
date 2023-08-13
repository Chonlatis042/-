from tkinter import *
from tkinter import messagebox
    #  หน้าต่าง
window = Tk()
window.title("GUI Tutorial")
window.geometry("500x300")
     #  สี
frame = Frame(window)
frame.config(background="silver")
frame.place(width=500, height=300, x=0, y=0)
      # ใส่ข้อความ(ตรงกลาง บนสุด)
Label(window, bg="gold", text="Chonlatis").pack(ipadx=5, ipady=5)

txt_input = Tk.stringVar()
      # ช่องใส่ข้อความ
Entry(window, textvariable=txt_input).pack()

      # ช่องใส่ข้อความ กำหนดเอง
text_area = Text(window, width=10, height=5)
text_area.pack()


     #ไส่ช่องไห้เหลือก   anchor=ทิศ 
chk1 = Checkbutton(window, bg="gold", text='ไอ้บ้า').pack(anchor=E, padx=10, pady=10)
chk2 = Checkbutton(window, bg="gold", text='ไอ้โง่').pack(anchor=W, padx=10, pady=10)
chk3 = Checkbutton(window, bg="gold", text='ไอ้ควาย').pack(anchor=S, padx=10, pady=10)

def chkLogin():
    msg = "Your input is " + tat_ipput.get()
    messagebox.showinfo("แจ้วเตือน",message=msg)

      # ไส่ปุ่ม
btn = Button(window, command=chkLogin, text="บันทึก", width=5, height=2)
btn.pack(padx=5, pady=10) # expand=True



window.mainloop()
