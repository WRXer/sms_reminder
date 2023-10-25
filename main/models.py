from django.db import models
from django.utils import timezone

import datetime


# Create your models here.
class Recipient(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    phone_number = models.CharField(max_length=15, unique=True)
    apartment = models.CharField(max_length=10, verbose_name='Квартира')
    send_time = models.TimeField(verbose_name='время отправки уведомления', default=datetime.time(8, 0))
    send_date = models.DateField(verbose_name="дата выполнения", default=timezone.now)
    is_active = models.BooleanField(default=True, verbose_name='Активен')

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.phone_number})"


    class Meta:
        verbose_name = 'Получатель'
        verbose_name_plural = 'Получатели'