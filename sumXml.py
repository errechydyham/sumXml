import urllib.request, urllib.parse, urllib.error 
import xml.etree.ElementTree as ET

#read the xml from a url 
u = input("Enter an url: ") 
d = urllib.request.urlopen(u).read() 

#turn the xml file into a tree to make access easier 
t = ET.fromstring(d)

#to store count and sum of the numbers 
c = 0 
s = 0 

#get all the count tags in the xml file 
tag = t.findall(".//count") 

for i in tag: 
    c += 1 
    s += int(i.text)  

#print the result 
print("counter of numbers :", c) 
print("sum of numbers :", s) 