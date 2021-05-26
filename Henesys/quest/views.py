from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.template.response import TemplateResponse
from .models import Quest
from django.utils import timezone
from accounts.models import ResourceManager, HenesysUser 
from pprint import pprint

def display_questlist(request):
   questlist = Quest.objects.all()
   current_time = timezone.localtime()
   for quest in questlist:
      if current_time > quest.due_date :
         quest.status = 'expired'
         quest.save()
      elif quest.status == 'expired' :
         quest.status = 'open'
         quest.closed_date = None
         quest.save()
      elif quest.status == 'open' :
         if quest.closed_date != None :
            quest.closed_date = None
            quest.save()
   sort = request.GET.get('sort', '')
   if sort == 'open':
        questlist = Quest.objects.filter(status='open').order_by('-pub_date')
   elif sort == 'closed':
        questlist = Quest.objects.filter(status='closed').order_by('-pub_date')
   elif sort == 'review':
        questlist = Quest.objects.filter(status='review').order_by('-pub_date')
   elif sort == 'rejected':
        questlist = Quest.objects.filter(status='rejected').order_by('-pub_date')
   elif sort == 'expired':
        questlist = Quest.objects.filter(status='expired').order_by('-pub_date')
   else:
        questlist = Quest.objects.order_by('-pub_date')
   return render(request,'display_questlist.html', {'questlist':questlist, 'sort':sort})

def display_detail_quest(request, pk):
   quest_obj = Quest.objects.get(pk=pk)
   publish_target = HenesysUser.objects.get(id=quest_obj.publish_target)
   user_id = str(request.user.id)
   current_time = timezone.localtime()
   return render(request, 'display_detail_quest.html', {'quest':quest_obj, 'user_id':user_id, 'publish_target':publish_target, 'current_time':current_time})   

def change_quest_status(request):
   if request.user.is_superuser:
      new_status = request.POST['new_status']
      pk = request.POST['pk']
      quest_obj = Quest.objects.get(pk=pk)
      quest_obj.status = new_status
      quest_obj.save()
   return render(request, 'display_detail_quest.html', {'new_status':new_status, 'pk':pk, 'quest':quest_obj})

def create_quest(request):
   userlist = User.objects.all()
   if request.user.is_superuser:
      if request.method == 'POST':
         publish_target_list=request.POST.getlist('selected_user')
         for target_id in publish_target_list:
            new_quest=Quest.objects.create(
               questname=request.POST['questname'],
               contents=request.POST['contents'],
               stars=request.POST['stars'],
               mana=request.POST['mana'],
               status='open',
               pub_date=timezone.localtime(),
               closed_date=None,
               due_date=request.POST['due_date'],
               publish_target=target_id
               )
         return redirect('display_questlist')
      return render(request, 'create_quest.html', {'userlist':userlist})

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
   if str(request.user.id) == quest_obj.publish_target:
      if request.method == 'POST':
         quest_obj.status = 'review'
         quest_obj.save()
         return redirect('display_detail_quest', pk=pk)
   return render(request, 'request_reward.html', {'quest': quest_obj})

def reject_quest(request, pk):
   if request.user.is_superuser:
      quest_obj = Quest.objects.get(pk=pk)
      if request.method == 'POST':
         quest_obj.status = 'rejected'
         quest_obj.save()
         return redirect('display_detail_quest', pk=pk)
   return render(request, 'reject_quest.html', {'quest': quest_obj}) 
   
def reward_quest(request, pk):
   if request.user.is_superuser:
      quest_obj = Quest.objects.get(pk=pk)
      if request.method == 'POST':
         stars_value = quest_obj.stars
         mana_value = quest_obj.mana
         target_id = quest_obj.publish_target
         ResourceManager.addStars(User.objects.get(id=target_id), stars_value)
         ResourceManager.addMana(User.objects.get(id=target_id), mana_value)
         quest_obj.status = 'closed'
         quest_obj.closed_date = timezone.localtime()
         quest_obj.save()     
         return redirect('display_detail_quest', pk=pk)
   return render(request, 'reward_quest.html', {'quest': quest_obj})     
