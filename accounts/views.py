from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render

def signup(request):
    if request.method == 'POST':