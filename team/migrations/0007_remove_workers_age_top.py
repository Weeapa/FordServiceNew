# Generated by Django 4.1.1 on 2022-09-15 19:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0006_workers_age_top'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workers',
            name='age_top',
        ),
    ]
