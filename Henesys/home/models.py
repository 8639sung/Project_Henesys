from django.db import models
from taggit.managers import TaggableManager

# Create your models here.
class Quest(models.Model):
    questname = models.CharField(max_length=50)
    contents = models.TextField()
    stars = models.PositiveBigIntegerField()
    mana = models.PositiveBigIntegerField()
    status = models.CharField(max_length=50)
    tag = TaggableManager()

    def _str_(self):
        return self.questname