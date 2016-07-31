import os, sys, re, fileinput

f = open("/Users//Younggi/dev/programming-5th/PostCode/서울특별시.utf8.txt", 'r')

slicing = f.read()

slicing_text = [i for i in slicing.split('|') if re.match(r'^\n\d{5}$', i)]

f.close()

g = open("/Users//Younggi/dev/programming-5th/PostCode/refined_서울특별시.utf8.txt", 'w')

for i in slicing_text:
    g.write(i)

g.close()