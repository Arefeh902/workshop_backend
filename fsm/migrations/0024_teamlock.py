# Generated by Django 3.1 on 2021-08-29 23:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fsm', '0023_auto_20210830_0320'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamLock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='lock', to='fsm.team')),
            ],
        ),
    ]