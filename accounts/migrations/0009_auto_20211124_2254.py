# Generated by Django 3.1 on 2021-11-24 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20211014_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='educationalinstitute',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
