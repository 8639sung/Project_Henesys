from django.shortcuts import render
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
