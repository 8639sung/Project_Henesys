# Generated by Django 3.2.2 on 2021-06-04 22:11

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='merchandise',
            fields=[
                ('refID', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(default='unnamed item', max_length=50)),
                ('paymentType', models.CharField(choices=[('star', 'Star Item'), ('mana', 'Mana Item'), ('free', 'Free Item')], default='free', max_length=4)),
                ('cost', models.PositiveBigIntegerField(default=0)),
                ('levelReq', models.PositiveIntegerField(default=0)),
                ('ageReq', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
