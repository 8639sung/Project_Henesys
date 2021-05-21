from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import ResourceManager, HenesysUser

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

def edit_profile(request):
    if request.method == "POST":
        id = request.user.id
        user_obj = HenesysUser.objects.get(id=id)
        user_obj.nickname=request.POST['nickname']
        user_obj.save()
        return redirect('home')
    return render(request,'edit_profile.html')

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
#    , {'error':' please corfirm password. '}