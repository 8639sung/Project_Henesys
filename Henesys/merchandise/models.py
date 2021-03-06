from django.db import models
import uuid

# Create your models here.
class merchandise(models.Model):
    refID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        max_length=50,
        default='unnamed item',
    )
    starItem = 'star'
    manaItem = 'mana'
    freeItem = 'free'
    paymentList = [
        (starItem,'Star Item'),
        (manaItem,'Mana Item'),
        (freeItem,'Free Item'),
    ]
    paymentType = models.CharField(
        max_length=4,
        choices=paymentList,
        default=freeItem,
    )

    cost = models.PositiveBigIntegerField(default=0)
    levelReq = models.PositiveIntegerField(default=0)
    ageReq   = models.PositiveIntegerField(default=0)
