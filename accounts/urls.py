from django.conf.urls import url
from django.contrib.auth.views import login

urlpatterns = [
    url(r'^login/$', login, name='login', kwargs={
        'template_name' : 'accounts/login.html',
    }), # kwargs로 넘겨줄 값은 https://github.com/django/django/blob/1.9.8/django/contrib/auth/views.py 에서 확인
]