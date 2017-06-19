#!/usr/bin/python
# -*- cpding: utf-8 -*-
import json
import sys
from collections import Counter
from colors import bcolors as bc
import fuzzy

reload(sys)
sys.setdefaultencoding('utf-8')

with open('doub.json', "r") as f:
    data = json.loads(f.read())
li = []
ids = []
for x in data:
    try:
        ap = ""
        s = ""
        ap = (
            str(x['title']) +
            x['propertyType'] + 
            x['dealer']['name'] + 
            str(x['roomCount']) +
            x['description'] +
            str(x['surface'])
            ).encode('utf-8')

        sdx = fuzzy.Soundex(len(ap));
        s = sdx(ap)
        li.append(s)
        ids.append(x['id'])
        #print s, x['title']
    except Exception as e:
        print bc.RED + str(e) + bc.RESET

i = 0

for x in li:
    print bc.GREEN + str(ids[i])
    print bc.BLUE + str(x) + bc.RESET
    i += 1
print i

print "processing deduplicate ..."
x = 0
doub = [];
print len(li)
while x < len(li):
    y = x + 1
    while y < len(li):
        if (li[x] == li[y]):
            doub.append(ids[x])
            print li[x] + "==" + li[y]
            print bc.RED + "__" +str(x) + "\n\n" + ids[x] + bc.RESET
            print "_-" + str(doub)
        y+=1
    x+=1
print bc.CYAN + "\n-_-_-_-_-_ "+ str(len(doub)) + " Doublons trouves _-_-_-_-_-\n" + bc.RESET

for x in doub:
    print bc.CYAN + str(x) + bc.RESET
