# Generated by Django 3.1 on 2021-12-30 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fsm', '0045_auto_20211209_1527'),
    ]

    operations = [
        migrations.AddField(
            model_name='description',
            name='is_spoilbox',
            field=models.BooleanField(default=False),
        ),
    ]
