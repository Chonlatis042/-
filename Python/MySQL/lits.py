"""
a = [ 3, 4, 2, 3, 4, 9, 4 , 7, 3, 4 ]
b = [ 'Google', 'Gmail', 'Youtube' ]
c = [8,2.1,'chonlatis',True]

print(a[2])
print(len(c))

for i in c:
 print(i)

for i in range(len(c)):
 print(i, c[i])


x = [1, 2, 3, 4 , 5, 6, 7, 8, 9 , 0]
print(x[:])        # สมาชิกยอยทั้งหมดในลีสต 
print(x[:5])       # สมาชิกยอยจากตำแหนงเริ่มต"นถึงตำแหนงที่ 4
print(x[5:])       # สมาชิกยอยจากตำแหนงที่ 5 ถึงตำแหนงสุดท"าย
print(x[3:6])      # สมาชิกยอยจากตำแหนงที่ 3 ถึงตำแหนงที่ 6
print(x[1:9:2])    # สมาชิกจากตำแหนงที่ 1 ถึงตำแหนงที่ 9 โดยเพิ่มคาทีละ 2
print(x[-1:-5:-1]) # สมาชิกจากตำแหนง -1 ถึงตำแหนง -5 โดยลดคาทีละ 1
print(x[:-3])      # สมาชิกยอยจากตำแหนงเริ่มต"น ถึงตำแหนง -3
print(x[-3:])      # สมาชิกยอยจากตำแหนงเริ่มต"นคือ -3 จนถึงตำแหนงสุดท"าย
print(x)           # สมาชิกยอยทั้งหมดในลีสต

a= ['ก','ค','ข']
a.sort()

print(a)
"""

import urllib
a = "https://th.wikipedia.org/"
b = "wiki/ประเทศไทย"
c = urllib.parse.quote(b)
url= a+c
s = urllib.request.urlopen(url).read().decode('utf-8', 'ignore')
print(s[0:300])





