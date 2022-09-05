# Generated by Django 4.1.1 on 2022-09-05 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('lastname', models.CharField(max_length=64)),
                ('position', models.CharField(max_length=64)),
                ('phone', models.CharField(max_length=20)),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d')),
            ],
        ),
    ]