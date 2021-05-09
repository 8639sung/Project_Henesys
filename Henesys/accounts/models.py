from django.conf import settings
from django.db import models

# Henesys User Model Implementation
# OneToOneField contains a reference to the User model in our HenesysUser model.

class HenesysUser(models.Model):
    # Associate HenesysUser model with User model
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE);
    fk_name = "user"

    # additional fields (see https://docs.djangoproject.com/en/3.2/ref/models/fields/)
    stars = models.PositiveBigIntegerField(default=0)
    mana  = models.PositiveBigIntegerField(default=0)

