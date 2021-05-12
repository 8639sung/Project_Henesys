from django.db import models

# Create your models here.
class Quest(models.Model):
    questname = models.CharField(max_length=50)
    contents = models.TextField()
    stars = models.PositiveBigIntegerField()
    mana = models.PositiveBigIntegerField()

    def _str_(self):
        return self.questname