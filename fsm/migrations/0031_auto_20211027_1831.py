# Generated by Django 3.1 on 2021-10-27 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fsm', '0030_event_accessible_after_closure'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrationform',
            name='certificate_name_X',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='registrationform',
            name='certificate_name_Y',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='registrationform',
            name='certificate_template',
            field=models.FileField(blank=True, null=True, upload_to='certificate_templates/'),
        ),
        migrations.AddField(
            model_name='registrationreceipt',
            name='certificate',
            field=models.FileField(blank=True, default=None, null=True, upload_to='certificates/'),
        ),
    ]
