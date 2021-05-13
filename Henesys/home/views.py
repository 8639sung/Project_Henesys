from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.template.response import TemplateResponse
from .models import Quest


#from pprint import pprint 

def home(request):
    userinfo = {}
 #   pprint(vars(name))
    userinfo['username'] = request.user.username
    userinfo['userstars'] = request.user.henesysuser.stars
    userinfo['usermana'] = request.user.henesysuser.mana
    return TemplateResponse(request, 'home.html', userinfo)

def test(request):
   return render(request, 'test.html')

def display_questlist(request):
   questlist = Quest.objects.all()
   return render(request,'display_questlist.html', {'questlist':questlist})

def display_detail_quest(request, pk):
   quest_obj = Quest.objects.get(pk=pk)
   return render(request, 'display_detail_quest.html', {'quest':quest_obj})   

def create_quest(request):
   if request.user.is_superuser:
      if request.method == 'POST':
         new_quest=Quest.objects.create(
            questname=request.POST['questname'],
            contents=request.POST['contents'],
            stars=request.POST['stars'],
            mana=request.POST['mana'],
            )
         return redirect('display_questlist')
      return render(request, 'create_quest.html')

def remove_quest(request, pk):
   if request.user.is_superuser:
      quest_obj = Quest.objects.get(pk=pk)
      if request.method == 'POST':
         quest_obj.delete()
         return redirect('display_questlist')
      return render(request, 'remove_quest.html', {'quest': quest_obj})

def edit_quest(request, pk):
   if request.user.is_superuser:
      quest_obj = Quest.objects.get(pk=pk)
      if request.method == 'POST':
         quest_obj.questname=request.POST['questname']
         quest_obj.contents=request.POST['contents']
         quest_obj.stars=request.POST['stars']
         quest_obj.mana=request.POST['mana']
         quest_obj.save()
         return redirect('display_detail_quest', pk=pk)
      return render(request,'edit_quest.html',{'quest':quest_obj})

def request_reward(request, pk):
   quest_obj = Quest.objects.get(pk=pk)
   if request.method == 'POST':
      #send this request to admin
      return render('display_questlist')
   return render(request, 'request_reward.html')
