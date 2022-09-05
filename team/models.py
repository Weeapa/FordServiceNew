from django.db import models

class Worker(models.Model):
    name = models.CharField(max_length=64)
    lastname = models.CharField(max_length=64)
    position = models.CharField(max_length=64)
    phone = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
