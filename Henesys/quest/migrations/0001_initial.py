# Generated by Django 3.2.2 on 2021-05-18 22:31

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questname', models.CharField(max_length=50)),
                ('contents', models.TextField()),
                ('stars', models.PositiveBigIntegerField()),
                ('mana', models.PositiveBigIntegerField()),
                ('status', models.CharField(max_length=50)),
                ('pub_date', models.DateTimeField()),
                ('closed_date', models.DateTimeField(blank=True, null=True)),
                ('due_date', models.DateTimeField(blank=True, null=True)),
                ('publish_target', models.CharField(max_length=50)),
                ('tag', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
        ),
    ]
