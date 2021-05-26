from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import auth


def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    else : return render(request, 'login.html')