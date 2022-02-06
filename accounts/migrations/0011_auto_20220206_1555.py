# Generated by Django 3.1 on 2022-02-06 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20220124_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='gender_type',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='school',
            name='school_type',
            field=models.CharField(blank=True, choices=[('Elementary', 'Elementary'), ('JuniorHigh', 'Juniorhigh'), ('High', 'High'), ('SchoolOfArt', 'Schoolofart')], max_length=15, null=True),
        ),
    ]
