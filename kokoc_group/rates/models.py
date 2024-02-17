from django.db import models


class Rate(models.Model):
    charcode = models.CharField(max_length=32, verbose_name='Код валюты')
    date = models.DateField(verbose_name='Дата обновления')
    rate = models.DecimalField(max_digits=9, decimal_places=4,
                               verbose_name='Курс')

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курс'
        ordering = ['-date', 'charcode']

    def __str__(self) -> str:
        return self.charcode
