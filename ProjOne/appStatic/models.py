from django.db import models


class FormHelp(models.Model):
    name = models.CharField(
        "Имя",
        max_length=150,
        null=False,
        blank=False
    )
    email = models.EmailField(
        "Почта",
        null=False,
        blank=False
    )
    text = models.TextField(
        "Комментарий",
        null=True,
        blank=True
    )
    dtime = models.DateTimeField(
        "Дата и время добавления",
        auto_now_add=True
    )
    
    status = models.CharField(
        "Статус",
        max_length=12,
        choices=[
            ("new", "Новый запрос"),
            ("processing", "В обработке"),
            ("success", "Обработан"),
        ],
        default="new"
    )
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "комметарий"
        verbose_name_plural = "Заявки"
        

class InfoNews(models.Model):
    title = models.CharField(
        "Заголовок",
        max_length=150,
        null=False,
        blank=False   
    )
    content = models.TextField(
        "Содержимое",
        null=True,
        blank=True
    )
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = "новость"
        verbose_name_plural = "Новости"
        