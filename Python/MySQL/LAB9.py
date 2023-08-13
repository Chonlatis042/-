  
    ###  การประกาศตัวแปรสตริง 
sp = '''
    www.
    '''
dp = """ 
    http
    """
print(sp+dp)

 '''    ###   การวนเข้าไปในสตริงเพื่อเข้าถึงสมาชิกย!อย 

s = "ABC"
for i in range(len(s)):
 print(s[i])
for i in range(3):
 print(i)

      ###  การแทนที่คำภายในตัวแปรสตริงด้วยคำสั่ง replace() 
print("information science".replace("information","data"))

      ###  การใช้คำสั่ง in เพื่อตรวจสอบข้อความภายในสตริง 
 s = "Information Science"
print("information" in s)
print("Information" in s)     

       ###  การเติมเลขศูนย+หน้าตัวเลขด้วยคำสั่ง zfill() 
print("5".zfill(4))
print(str(5).zfill(8))

       ###   การลบเครื่องหมาย white space ด้านหน้าและหลังตัวแปรสตริงด้วยคำสั่ง strip()
a = " 000 ".strip()
b = " 000 ".lstrip() #ซ้าย
c = " 000 ".rstrip() #ขวา
print("%s\n%s\n%s"%(a,b,c))

       ###  การแยกสตริงด้วยคำสั่ง split() 
s = "Google Gmail Youtube"
z = s.split(" ")
print(z)
y = s.rsplit(" ",1)
print(y)
'''


s = "Informåtion Science"
print(s.encode(encoding="",errors="replace"))



