'''
# ตัดเกรด
import math
a = int(input())
if a >= 50:
    print("สอบผ่าน")
elif a < 50:
    print("สอบตก")



# แม่สูตรคูณ
number = int(input())
for i in range(1,13):
    result = number*i
    print("%d x %d = %d"%(number,i,result))
'''

#สร้างฟังก์ชัน subtract()

def subtract(a,b):
    adder = a-b
    return adder
t = subtract(9,11)
print (t)



