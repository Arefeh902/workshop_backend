# Generated by Django 3.0.8 on 2020-09-11 08:12

from django.db import migrations, models
import fsm.models


class Migration(migrations.Migration):

    dependencies = [
        ('fsm', '0006_auto_20200910_2135'),
    ]

    operations = [
        migrations.AddField(
            model_name='fsmstate',
            name='type',
            field=models.CharField(choices=[('withMentor', 'withMentor'), ('withoutMentor', 'withoutMentor')], default=fsm.models.StateType['withoutMentor'], max_length=40),
        ),
    ]