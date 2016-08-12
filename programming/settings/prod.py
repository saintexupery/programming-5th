from .common import *

DEBUG = False # debug는 개발용이며, 꺼주지 않는다면 비밀번호, 쿼리셋 등 모든 데이터를 유저가 열람할 수 있다.
ALLOWED_HOSTS = ['*'] # 어떤 domain name을 허용할 것인가. ex) ['myphoto.kr', 'festi.kr']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql', # sqlite3는 수TB가 저장이 가능하나 여러명이 동시 접근 불가능
        'NAME': 'ubuntu',
        'USER': 'ubuntu',
        'PASSWORD': 'withaskdjango!',
        'HOST': '127.0.0.1', # localhost:8000과는 완전히 다르다.
    }
}