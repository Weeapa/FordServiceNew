# Generated by Django 4.1.1 on 2022-09-05 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0002_rename_worker_workers'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='workers',
            options={'verbose_name': 'Работник', 'verbose_name_plural': 'Работники'},
        ),
        migrations.AlterField(
            model_name='workers',
            name='lastname',
            field=models.CharField(max_length=64, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='workers',
            name='name',
            field=models.CharField(max_length=64, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='workers',
            name='phone',
            field=models.CharField(max_length=20, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='workers',
            name='photo',
            field=models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name=''),
        ),
        migrations.AlterField(
            model_name='workers',
            name='position',
            field=models.CharField(max_length=64, verbose_name='Должность'),
        ),
    ]