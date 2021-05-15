from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

class HenesysUser(models.Model):

    # Associate HenesysUser model with User model
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE);
    #fk_name = "user"

    # additional fields (see https://docs.djangoproject.com/en/3.2/ref/models/fields/)
    stars = models.PositiveBigIntegerField(default=0)
    mana  = models.PositiveBigIntegerField(default=0)
    temp  = models.PositiveBigIntegerField(default=0)


@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:     
        HenesysUser.objects.create(user=instance)
    instance.henesysuser.save()

class ResourceManager():
    @classmethod
    def getStarMultiplier(self):
        return 1

    @classmethod
    def getManaMultiplier(self):
        return 1        

    @classmethod
    def addStars(self, user, vStars):
        multiplier = self.getStarMultiplier()
        user.henesysuser.stars += multiplier*vStars
        user.henesysuser.save()

    @classmethod
    def addMana(self, user, vMana):
        multiplier = self.getManaMultiplier()
        user.henesysuser.mana += multiplier*vMana
        user.henesysuser.save()