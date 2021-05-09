from django.db import models

class User(models.Model):
    username = models.CharField(max_length=40000)
    password = models.EmailField(max_length=40000)
    password1 = models.CharField(max_length=40000)
    password2 = models.CharField(max_length=40000)