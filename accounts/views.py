from django.conf import settings
from django.shortcuts import redirect, render
from .forms import SignupForm

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(settings.LOGIN_URL) # 관련 설정은 https://github.com/django/django/blob/1.9.8/django/contrib/auth/views.py 에서 직접 해줄 수 있다. global settings를 받아 온 후 우리의 settings로 overwrite하는 것이기 때문
    else:
        form = SignupForm()

    return render(request, 'accounts/signup_form.html', {
        'form': form,
    })