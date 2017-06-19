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
with open('doub.json') as f:
    data = json.loads(f.read())

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
        print bc.RED + str(e) + str(x['id']) + bc.RESET
        data.pop(y)
    y+=1
i = 0
for x in li:
    print bc.GREEN + str(ids[i])
    print bc.BLUE + str(x) + bc.RESET
    i += 1
print i
print bc.BLUE + "processing deduplicate ..." + bc.RESET
print len(li)
x = 0
while x < len(li):
    y = x + 1
    while y < len(li):
        if (li[x] == li[y]):
            doub.append(ids[y])
        y+=1
    x+=1
print bc.BLUE
print "\n-_-_-_-_-_ "+ str(len(doub)) + " Doublons trouves _-_-_-_-_-\n"
print bc.RESET
for x in doub:
    print bc.CYAN + str(x) + bc.RESET
