from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('display_userinfo/', views.display_userinfo, name='display_userinfo'),
    path('edit_userinfo/', views.edit_userinfo, name='edit_userinfo'),
    path('addStarsWrapper/', views.addStarsWrapper, name='addStarsWrapper'),
    path('addManaWrapper/', views.addManaWrapper, name='addManaWrapper'),
]