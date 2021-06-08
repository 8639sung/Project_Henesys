from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import auth
from .nmap_scan import *


def home(request):
    if request.user.is_authenticated:
        online_user_list = scan()
        return render(request, 'home.html', {'online_user_list':online_user_list})
    else : 
        return render(request, 'login.html')