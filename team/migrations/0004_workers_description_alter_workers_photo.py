# Generated by Django 4.1.1 on 2022-09-05 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0003_alter_workers_options_alter_workers_lastname_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='workers',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание сотрудника'),
        ),
        migrations.AlterField(
            model_name='workers',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d', verbose_name='Фото'),
        ),
    ]