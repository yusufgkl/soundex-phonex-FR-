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
#with open('2017-03-29_annonces_paris.json') as f:
with open('doub.json') as f:
    data = json.loads(f.read())
i=0
for d in data:
    i+=1
print i
i = 0
print bc.BLUE + "Cleaning ..." + bc.RESET
for o in data:
    if not 'title' in o:
        data.pop(i)
    if not 'propertyType' in o:
        data.pop(i)
    if not 'dealer' in o:
        data.pop(i)
    if not 'roomCount' in o:
        data.pop(i)
    if not 'description' in o:
        data.pop(i)
    if not 'surface' in o:
        data.pop(i)
    i += 1
i = 0

for x in data:
    try:
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

while x < len(li):
    y = x + 1
    while y < len(li):
        if (li[x] == li[y]):
            doub.append(ids[y])
            try:
                del data[x]
            except Exception as e:
                print bc.RED + str(e) + bc.RESET
        y+=1
    x+=1

print bc.BLUE
print "\n-_-_-_-_-_ "+ str(len(doub)) + " Doublons trouves _-_-_-_-_-\n"
print bc.RESET

for x in doub:
   print bc.CYAN + str(x) + bc.RESET

print " ___ _ _ _ _ __ " + str(len(data))

for x in range(len(data)):
   print bc.CYAN + str(x) + bc.RESET

clean = open("clean_final.json", 'w')
clean.write(json.dumps(data, indent=4))

with open('clean_final.json') as c:
    clean = json.loads(c.read())
i=0
for d in clean:
    i+=1
print i

