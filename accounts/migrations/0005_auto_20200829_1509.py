# Generated by Django 3.0.8 on 2020-08-29 10:39

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200829_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]