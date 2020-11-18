# Generated by Django 3.0.8 on 2020-11-16 22:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fsm', '0007_playerworkshop_last_visit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playerworkshop',
            name='current_state',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='player_workshop', to='fsm.FSMState'),
        ),
    ]