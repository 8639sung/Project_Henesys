from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.template.response import TemplateResponse
from .models import Quest
from django.utils import timezone
#from pprint import pprint 
#   pprint(vars(name))

def test(request):
   return render(request, 'test.html')

def display_questlist(request):
   questlist = Quest.objects.all()
   sort = request.GET.get('sort', '')
   if sort == 'open':
        questlist = Quest.objects.filter(status='open').order_by('-pub_date')
   elif sort == 'closed':
        questlist = Quest.objects.filter(status='closed').order_by('-pub_date')
   elif sort == 'review':
        questlist = Quest.objects.filter(status='review').order_by('-pub_date')
   elif sort == 'rejected':
        questlist = Quest.objects.filter(status='rejected').order_by('-pub_date')
   else:
        questlist = Quest.objects.order_by('-pub_date')
   return render(request,'display_questlist.html', {'questlist':questlist, 'sort':sort})

def display_detail_quest(request, pk):
   quest_obj = Quest.objects.get(pk=pk)
   return render(request, 'display_detail_quest.html', {'quest':quest_obj})   

def change_quest_status(request):
   new_status = request.POST['new_status']
   pk = request.POST['pk']
   quest_obj = Quest.objects.get(pk=pk)
   quest_obj.status = new_status
   quest_obj.save()
   return render(request, 'display_detail_quest.html', {'new_status':new_status, 'pk':pk, 'quest':quest_obj})

def create_quest(request):
   if request.user.is_superuser:
      if request.method == 'POST':
         new_quest=Quest.objects.create(
            questname=request.POST['questname'],
            contents=request.POST['contents'],
            stars=request.POST['stars'],
            mana=request.POST['mana'],
            status='open',
            pub_date=timezone.localtime(),
            closed_date=None,
            due_date=request.POST['due_date'],
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
         quest_obj.due_date=request.POST['due_date']
         quest_obj.save()
         return redirect('display_detail_quest', pk=pk)
      return render(request,'edit_quest.html',{'quest':quest_obj})

def request_reward(request, pk):
   quest_obj = Quest.objects.get(pk=pk)
   if request.method == 'POST':
      #send this request to admin
      return render('display_questlist')
   return render(request, 'request_reward.html')
