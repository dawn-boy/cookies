# IMPORTS 
import os

# FORMATTING
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

# WRITING THE FORMATTED DATA
with open("cookies",'w') as cookiesFile:
    cookiesFile.write(finalStr)

# MAKING A .dat FILE SO FORTUNE CAN SELECT A HIGHLIGHT AT RANDOM
os.system('strfile -c % cookies cookies.dat')
