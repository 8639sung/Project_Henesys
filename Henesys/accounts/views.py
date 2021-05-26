from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import ResourceManager, HenesysUser
from django.template.response import TemplateResponse

 
def signup(request):
    if request.method == "POST":
        if request.POST["password1"] == request.POST["password2"]:
            user = User.objects.create_user(
                username=request.POST["username"],
                password=request.POST["password1"],
                usernickname=request.POST["nickname"]
                )
            auth.login(request,user)
            return redirect('home')
        return render(request,'signup.html')
    return render(request,'signup.html')

def display_userinfo(request):
    userinfo = {}
    userinfo['nickname'] = request.user.henesysuser.nickname
    userinfo['ID'] = request.user.username
    userinfo['userstars'] = request.user.henesysuser.stars
    userinfo['usermana'] = request.user.henesysuser.mana
    return TemplateResponse(request, 'display_userinfo.html', userinfo)
    
def edit_userinfo(request):
    if request.method == "POST":
        id = request.user.id
        user_obj = HenesysUser.objects.get(id=id)
        user_obj.nickname=request.POST['nickname']
        user_obj.save()
        return redirect('display_userinfo')
    return render(request,'edit_userinfo.html')

def login(request):
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request,'login.html')
    else :
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')

def addStarsWrapper(request):
    ResourceManager.addStars(request.user, stars_value)
    return redirect('home')

def addManaWrapper(request):
    ResourceManager.addMana(request.user, mana_value)
    return redirect('home')    
