import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "programming.settings")
import django
django.setup()

import csv

CSV_PATH = 'PostCode/서울특별시.utf8.txt'

reader = csv.reader(open(CSV_PATH, 'rt'), delimiter='|') # encoding='cp949'

from blog.models import ZipCode

columns = next(reader) # 컬럽 제목 뽑아내는 것

zip_code_list = []

for idx, row in enumerate(reader):
    data = dict(zip(columns, row))
    zip_code =
    (
        city=data['시도'], road=data['도로명'], dong=data['법정동명'],
        gu=data['시군구'], code=data['새우편번호'])

    zip_code_list.append(zip_code)

# zip_code_list = list(set(zip_code_list)) 클래스의 같고 다름을 비교할 수 없다. 클래스 인스턴스를 생성하기 전에 딕셔너리로 받아서 중복처리 이후에 클래스 인스턴스를 받아야함.

print('zip_code size : {}'.format(len(zip_code_list)))
ZipCode.objects.bulk_create(zip_code_list, 100)







