from django.db import models


class Workers(models.Model):
    name = models.CharField(max_length=64, verbose_name='Имя')
    lastname = models.CharField(max_length=64, verbose_name='Фамилия')
    position = models.CharField(max_length=64, verbose_name='Должность')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Фото', blank=True)

    def __str__(self):
        return self.name

    class Meta():
        verbose_name = "Работник"
        verbose_name_plural = "Работники"
