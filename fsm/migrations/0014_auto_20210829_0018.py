# Generated by Django 3.1 on 2021-08-28 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fsm', '0013_delete_mainstate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='helpstate',
            name='fsmstate_ptr',
        ),
        migrations.RemoveField(
            model_name='helpstate',
            name='statee',
        ),
        migrations.DeleteModel(
            name='FSMState',
        ),
        migrations.DeleteModel(
            name='HelpState',
        ),
    ]
