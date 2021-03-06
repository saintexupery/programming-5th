import re
import os
import requests
import xmltodict
from uuid import uuid4
from django.utils import timezone
from django.conf import settings
from django.forms import ValidationError
from django.utils.deconstruct import deconstructible

def lnglat_validator(value):
    if not re.match(r'^(\d+\.?\d*),(\d+\.?\d*)$', value):
        raise ValidationError('Invalid LngLat Type')

''' 이 방식은 마이그레이션 적용이 안됨
def min_length_validator(min_length):
    def wrap(value):
        if len(value) < min_length:
            raise ValidationError('{}글자 이상을 입력해주세요'.format(min_length))
    return wrap
'''

@deconstructible
class MinLengthValidator(object):
    def __init__(self, min_length):
        self.min_length = min_length

    def __call__(self, value):
        if len(value) < self.min_length:
            raise ValidationError('{}글자 이상을 입력해주세요'.format(self.min_length))

'''
def max_length_validator(max_length):
    def wrap(value):
        if len(value) > max_length:
            raise ValidationError('{}글자 이하를 입력해주세요'.format(max_length))

    return wrap
'''

def MaxLengthValidator(object):
    def __init__(self, max_length):
        self.max_length = max_length

    def __call__(self, value):
        if len(value) > self.max_length:
            raise ValidationError('{}글자 이하를 입력해주세요.'.format(self.max_length))


def phone_number_validator(value):
    if not re.match(r'^01[016789][1-9]\d{6,7}$', value):
        raise ValidationError('휴대폰 번호를 입력해주세요.')


h = open("./PostCode/refined_서울특별시.utf8.txt", 'r')
raw_postcode = h.read()
refined_postcode = raw_postcode.split('\n')
real_refined_postcode = list(set(refined_postcode))
real_refined_postcode[0] = real_refined_postcode[0][1:]
h.close()

def post_code_validator(value):
    if not re.match(r'^[0123456]\d{4}$', value):
        raise ValidationError('알맞은 형태의 우편번호를 입력해주세요.')

    if not value in real_refined_postcode:
        raise ValidationError('존재하지 않는 우편번호입니다.')


@deconstructible
class ZipCodeValidator(object):
    '우편번호 체계안내 : http://www.koreapost.go.kr/kpost/sub/subpage.jsp?contId=010101040100'

    def __init__(self, is_check_exist=False):
        self.is_check_exist = is_check_exist

    def __call__(self, zip_code):
        if not re.match(r'^\d{5,6}$', zip_code):
            raise ValidationError('5자리 혹은 6자리 숫자로 입력해주세요.')

        if self.is_check_exist:
            self.check_exist(zip_code)

    def check_exist_from_db(self, zip_code):
        from blog.models import ZipCode
        if not ZipCode.objects.filter(code=zip_code).exists():
            raise ValidationError('입력하신 우편번호가 존재하지 않습니다.')

    def check_exist(self, zip_code):
        '우체국 open api : http://biz.epost.go.kr/customCenter/custom/custom_10.jsp'

        params = {
            'regkey' : settings.EPOST_API_KEY,
            'target' : 'postNew',
            'query' : zip_code,
        }
        xml = requests.get('http://biz.epost.go.kr/KpostPortal/openapi', params=params).text
        response = xmltodict.parse(xml)
        try:
            error = response['error']
        except KeyError:
            pass
        else:
            raise ValidationError('[{error_code}] {message}'.format(**error))


def get_file_path(instance, filename):
    name = uuid4().hex
    extension = os.path.splitext(filename)[-1].lower()
    # splitext = split extension, 경로와 확장자를 나누어 튜플로 반환)
    # 경로를 반환할 때 파일의 확장자는 변하면 안되기 때문에 이 메소드를 사용.
    return os.path.join(name[:3], name[3:6], name[6:] + extension) # name[:3] + '/' + name[3:6] + '/' + name[6:] + 확장자. os.path.join에서는 ,는 /로 연결되고 +는 그대로 뒤에 이어 붙인다.







