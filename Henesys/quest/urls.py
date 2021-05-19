from django.urls import path
from . import views

urlpatterns = [
    path('display_questlist/', views.display_questlist, name='display_questlist'),
    path('display_questlist/<int:pk>', views.display_detail_quest, name='display_detail_quest'),
    path('create_quest/', views.create_quest, name='create_quest'),
    path('display_questlist/<int:pk>/remove', views.remove_quest, name='remove_quest'),
    path('display_questlist/<int:pk>/edit', views.edit_quest, name='edit_quest'),
    path('display_questlist/<int:pk>/request', views.request_reward, name='request_reward'),
    path('display_questlist/<int:pk>/reject', views.reject_quest, name='reject_quest'),
    path('display_questlist/<int:pk>/reward', views.reward_quest, name='reward_quest'),
    path('change_quest_status', views.change_quest_status,name='change_quest_status'),
]