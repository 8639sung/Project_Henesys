from django.db import models
from taggit.managers import TaggableManager
from django.utils import timezone

# Create your models here.
class Quest(models.Model):
    questname = models.CharField(max_length=50)
    contents = models.TextField()
    stars = models.PositiveBigIntegerField()
    mana = models.PositiveBigIntegerField()
    status = models.CharField(max_length=50)
    pub_date = models.DateTimeField()
    closed_date = models.DateTimeField(null=True, blank=True)
    due_date = models.DateTimeField(null=True, blank=True)
    tag = TaggableManager()


    def _str_(self):
        return self.questname