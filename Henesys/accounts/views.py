from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.template.response import TemplateResponse
#from pprint import pprint 

def home(request):
    args = {}
 #   pprint(vars(name))
    args['username'] = request.user.username
    args['userstars'] = request.user.henesysuser.stars
    args['usermana'] = request.user.henesysuser.mana
    return TemplateResponse(request, 'home.html', args)

def signup(request):
    if request.method == "POST":
        if request.POST["password1"] == request.POST["password2"]:
            user = User.objects.create_user(
                username=request.POST["username"],password=request.POST["password1"])
            auth.login(request,user)
            return redirect('home')
        return render(request,'signup.html', {'error':' please corfirm password. '})
    return render(request,'signup.html')

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