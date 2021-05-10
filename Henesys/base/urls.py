from django.urls import path
from . import views

urlpatterns = [
    path('base/', views.home, name='base'),
    path('home/', views.home, name='home'),
]