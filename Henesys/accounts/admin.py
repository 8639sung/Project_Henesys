from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
# Register your models here.



from .models import HenesysUser

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class HenesysUserInline(admin.StackedInline):
    model = HenesysUser
    can_delete = False
    verbose_name_plural = 'HenesysUsers'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (HenesysUserInline,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)