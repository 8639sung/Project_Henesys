from django.contrib.auth.models import User
from django.contrib import auth
from django.template.response import TemplateResponse

def home(request):
    userinfo = {}
 #   pprint(vars(name))
    userinfo['username'] = request.user.username
    userinfo['userstars'] = request.user.henesysuser.stars
    userinfo['usermana'] = request.user.henesysuser.mana
    return TemplateResponse(request, 'home.html', userinfo)