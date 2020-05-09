from django.db import models


class FTTx(models.Model):
    name = models.TextField(
        verbose_name='Название',
    )
    volokno = models.PositiveIntegerField(
        verbose_name='Кол-во волокн',
    )
    kN= models.TextField(
        verbose_name='кН',
    )
    price = models.PositiveIntegerField(
        verbose_name='Цена',
    )
    link = models.URLField(
        verbose_name='Ссылка',
        unique=True,
    )

    def __str__(self):
        return f'#{self.pk} {self.name}'

    class Meta:
        verbose_name = 'FTTx'
        verbose_name_plural = 'FTTx'


class ADSS(models.Model):
    name = models.TextField(
        verbose_name='Название',
    )
    volokno = models.PositiveIntegerField(
        verbose_name='Кол-во волокн',
    )
    kN= models.TextField(
        verbose_name='кН',
    )
    price = models.PositiveIntegerField(
        verbose_name='Цена',
    )
    link = models.URLField(
        verbose_name='Ссылка',
        unique=True,
    )

    def __str__(self):
        return f'#{self.pk} {self.name}'

    class Meta:
        verbose_name = 'Подвесной самонесущий, ADSS'
        verbose_name_plural = 'Подвесной самонесущий, ADSS'