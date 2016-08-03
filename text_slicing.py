import os, sys, re, fileinput

# txt는 인코딩 명시 방법이 없다. cp949 방식인 상황에서, 기본적으로 utf8이 endcoding parameter로 지정되어 있어, open("경로", 'rt', encoding="cp949")를 작성해주어야함
f = open("./PostCode/서울특별시.utf8.txt", 'r')

slicing = f.read()

slicing_text = [i for i in slicing.split('|') if re.match(r'^\n\d{5}$', i)]

f.close()

g = open("./PostCode/refined_서울특별시.utf8.txt", 'w')

for i in slicing_text:
    g.write(i)

g.close()