# Generated by Django 3.1 on 2022-04-03 00:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fsm', '0050_event_crispwebsiteid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='crispWebsiteId',
        ),
    ]
