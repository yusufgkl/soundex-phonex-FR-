#!/usr/bin/python
# -*- coding: utf-8 -*-
#  -----------------------------------
# | Exercice d'analyse de data        |
# |                                   |
# | Yusuf Gokol - yusufgkl@gmail.com  |
#  -----------------------------------

import json
import sys
from colors import bcolors as bc
from phonex import phonex
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
        alph = ""
        pnx = ""
        alph = (str(x['title']) +
                str(x['propertyType']) +
                str(x['dealer']['name']) +
                str(x['roomCount']) +
                str(x['description']) +
                str(x['surface'])
                ).encode('utf-8')
        alph = re.sub('[^0-9a-zA-Z]+', '*', alph) #alphanumerique, nombre = problemes
        pnx = phonex(alph) # application de l'algo de soundex/phonex
        li.append([pnx, str(x['id'])])
        ids.append(x['id'])
    except Exception as e:
        #print bc.RED + str(e) + "  " + str(x['id']) + bc.RESET
        del data[y]
    y+=1

print bc.BLUE + "Cleaning done\n" + bc.RESET

print bc.BLUE + "\nprocessing deduplicate ..." + bc.RESET
x = 0
y = 0

doub = set(tuple(elem) for elem in li)
set (doub) #del les doublons dans doub
doub = list(elem for elem in doub)

#del les doublons dans data
g = 0
print "\n\n"
for e in data:
    if doub[0][1] in e:
        del data[g]
    g+=1

clean_file = open("clean_final.json", 'w')
clean_file.write(json.dumps(data, indent=4))
clean_file.close()

#print bc.CLEAN #clean le screen si voulu
print "\n\n"
for y in doub:
    print y[1]
print bc.CYAN + """
  ____                                __     
 /\  _`\                             /\ \    
 \ \ \/\ \    ___     ___      __    \ \ \   
  \ \ \ \ \  / __`\ /' _ `\  /'__`\   \ \ \  
   \ \ \_\ \/\ \L\ \/\ \/\ \/\  __/    \ \_\ 
    \ \____/\ \____/\ \_\ \_\ \____\    \/\_\\
     \/___/  \/___/  \/_/\/_/\/____/     \/_/
                                                               
                                                                                                           
""" + bc.RESET
