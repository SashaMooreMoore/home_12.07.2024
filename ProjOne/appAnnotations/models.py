from django.db import models


class Info(models.Model):
    title = models.CharField(
        verbose_name="Название",
        max_length=150,
        null=True,
        blank=True
    )
    balance = models.FloatField(
        verbose_name="Баланс",
        default=0.0
    )

    balance_two = models.FloatField(
        verbose_name="Второй баланс",
        default=340.50
    )
    
    class Meta:
        verbose_name = "информацию"
        verbose_name_plural = "Информация"

    def __str__(self):
        return f"Баланс: {self.balance}"


class Bank(models.Model):
    first_name = models.CharField(
        verbose_name="Имя",
        max_length=100
    )
    balance = models.FloatField(
        verbose_name="Баланс"
    )
    percent = models.IntegerField(
        verbose_name="Процент на остаток",
        choices=[
            (2, '2%'),
            (4, '4%'),
            (10, '10%'),
            (16, '16%'),
        ],
        default=4
    )
    def __str__(self):
        return self.first_name
    
    class Meta:
        verbose_name = 'пользователя'
        verbose_name_plural = 'Накопительный счёт'