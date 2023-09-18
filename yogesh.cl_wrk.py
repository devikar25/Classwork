import re
a = 'i am in a pune is in maharashtra and maharashtra in india and india is in asia'
b = ['pune','india','is','maha']
for i in b:
 print (re.findall(i,a))
