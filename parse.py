#!/usr/bin/python
# -*- cpding: utf-8 -*-
# Yusuf Gokol - yusufgkl@gmail.com
import json
import sys
from collections import Counter
from colors import bcolors as bc
from phonex import phonex as fnx
import re

reload(sys)
sys.setdefaultencoding('utf-8')

li = []
ids = []
i = 0
doub = []
y = 0
with open('2017-03-29_annonces_paris.json') as f:
    data = json.loads(f.read())
i=0
#for d in data:    #DEBUG
#    i+=1
#print i
i = 0
print bc.BLUE + "Cleaning ..." + bc.RESET
i = 0

for x in data:
    try:
        if not 'title' in x:
            data.pop(y)
        if not 'propertyType' in x:
            data.pop(y)
        if not 'dealer' in x:
            data.pop(y)
        if not 'roomCount' in x:
            data.pop(y)
        if not 'description' in x:
            data.pop(y)
        if not 'surface' in x:
            data.pop(y)
        ap = ""
        s = ""
        ap = (str(x['title']) +
                str(x['propertyType']) +
                str(x['dealer']['name']) +
                str(x['roomCount']) +
                str(x['description']) +
                str(x['surface'])
                ).encode('utf-8')
        ap = re.sub('[^0-9a-zA-Z]+', '*', ap)
        s = fnx(ap)
        li.append(s)
        ids.append(x['id'])
    except Exception as e:
        print bc.RED + str(e) + "  " + str(x['id']) + bc.RESET
        del data[y]
    y+=1
i = 0

x = 0
for x in li:
    print bc.GREEN + str(ids[i])
    print bc.BLUE + str(x) + bc.RESET
    i += 1
print i
print len(li)
print bc.BLUE + "processing deduplicate ..." + bc.RESET
x = 0
y = 0

clean = set(li)

print len(li)
print len (data)

doub = set(li)


'''
while x < len(li):
    y = x + 1
    while y < len(li):
        if (li[x] == li[y]):
            doub.append(ids[y])
            try:
                del data[x]
            except Exception as e:
                print bc.RED + '.' + bc.RESET
                data.pop(y)
                #print bc.RED + str(e) + bc.RESET
        y+=1
    x+=1
'''
print bc.BLUE
print "\n"+ str(len(doub)) + " Doublons trouves\n"
print bc.RESET
exit()
for x in doub:
   print bc.CYAN + str(x) + bc.RESET

for x in range(len(doub)):
   print bc.CYAN + str(x) + bc.RESET

clean = open("clean_final2.json", 'w')
clean.write(json.dumps(data, indent=4))
#print bc.CLEAN
print bc.CYAN + """
  ____                                __     
 /\  _`\                             /\ \    
 \ \ \/\ \    ___     ___      __    \ \ \   
  \ \ \ \ \  / __`\ /' _ `\  /'__`\   \ \ \  
   \ \ \_\ \/\ \L\ \/\ \/\ \/\  __/    \ \_\ 
    \ \____/\ \____/\ \_\ \_\ \____\    \/\_\\
     \/___/  \/___/  \/_/\/_/\/____/     \/_/
                                                               
                                                                                                           
""" + bc.RESET
