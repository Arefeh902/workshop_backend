# Generated by Django 3.0.8 on 2020-08-24 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20200823_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]