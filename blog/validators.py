import re
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
def MinLengthValidator(object):
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
            raise ValidationError('{}글자 이하를 입력해주세요'.format(self.max_length))


def phone_number_validator(value):
    if not re.match(r'^01[016789][1-9]\d[6, 7]$', value):
        raise ValidationError('휴대폰 번호를 입력해주세요')













