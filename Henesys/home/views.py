from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.template.response import TemplateResponse
from .models import Quest
#from pprint import pprint 

def home(request):
    args = {}
 #   pprint(vars(name))
    args['username'] = request.user.username
    args['userstars'] = request.user.henesysuser.stars
    args['usermana'] = request.user.henesysuser.mana
    return TemplateResponse(request, 'home.html', args)

def test(request):
   return render(request, 'test.html')

def display_questlist(request):
   questlist = Quest.objects.all()
   return render(request,'display_questlist.html', {'questlist':questlist})

def display_detail_quest(request, pk):
   quest_obj = Quest.objects.get(pk=pk)
   return render(request, 'display_detail_quest.html', {'quest':quest_obj})   

def create_quest(request):
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
    quest_obj = Quest.objects.get(pk=pk)
    if request.method == 'POST':
        quest_obj.delete()
        return redirect('display_questlist')
    return render(request, 'remove_quest.html', {'quest': quest_obj})

def edit_quest(request, pk):
   quest_obj = Quest.objects.get(pk=pk)
   if request.method == 'POST':
      quest_obj.questname=request.POST['questname']
      quest_obj.contents=request.POST['contents']
      quest_obj.stars=request.POST['stars']
      quest_obj.mana=request.POST['mana']
      quest_obj.save()
      return redirect('display_detail_quest', pk=pk)

   return render(request,'edit_quest.html',{'quest':quest_obj})
