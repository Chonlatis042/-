import urllib, urllib.request
url = " https://it.northbkk.ac.th/thailis-10000.txt"
thesis = urllib.request.urlopen(url).read().decode('utf-8', 'ignore').split("\n")
q = "มืออาชีพ"
result = list(filter(lambda i:q in i, thesis))
print("พบ '%s' ทั้งหมด %d เล*ม"%(q,len(result)))
for i in range(len(result)):
 print("%d) %s"%(i+1,result[i]))