# Generated by Django 3.1 on 2020-08-30 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fsm', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fsmedge',
            name='text',
            field=models.TextField(null=True),
        ),
    ]
