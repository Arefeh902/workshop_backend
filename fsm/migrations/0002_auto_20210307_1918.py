# Generated by Django 3.0.8 on 2021-03-07 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fsm', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_cost',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='event',
            name='event_type',
            field=models.CharField(choices=[('team', 'Team'), ('individual', 'Individual')], default='individual', max_length=40),
        ),
        migrations.AddField(
            model_name='event',
            name='has_selection',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='event',
            name='team_size',
            field=models.IntegerField(default=3),
        ),
    ]