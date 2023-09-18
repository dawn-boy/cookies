import os
from pprint import pprint
with open("My Clippings.txt",'r') as clipping:
    data = '==========\n'
    data += clipping.read()

changes1 = data.splitlines()

finalStr = ''

onDisplay = True 
for element in changes1:
    if element == '==========':
        onDisplay = False
    elif element == '':
        onDisplay = True
    if onDisplay == True:
        if element != '':
            finalStr += element
            finalStr += '\n%\n'
with open("cookies",'w') as cookiesFile:
    cookiesFile.write(finalStr)

os.system('strfile -c % cookies cookies.dat')
