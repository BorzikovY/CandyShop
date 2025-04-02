from django.db import models


class Candy(models.Model):
    class Meta:
        verbose_name = "Конфета"
        verbose_name_plural = "Конфеты"

    name = models.CharField(
        verbose_name="Название",
        max_length=32,
        null=False,
        blank=True,
        unique=True
    )
    description = models.TextField(
        verbose_name="Описание",
        null=False,
        blank=True,
    )
    price = models.DecimalField(
        verbose_name="Цена за 100 грамм",
        max_digits=10,
        decimal_places=2,
        null=False,
        blank=True
    )
    
    def __str__(self) -> str:
        return self.name


class Order(models.Model):
    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    address = models.CharField(
        verbose_name="Адрес доставки конфет",
        max_length=1000,
        null=False,
        blank=True
    )
    date_time = models.DateTimeField(
        verbose_name="Дата заказа",
        auto_now_add=True
    )

    def __str__(self) -> str:
        return str(self.date_time)


class OrderedCandy(models.Model):
    class Meta:
        verbose_name = "Заказанная конфета"
        verbose_name_plural = "Заказанные конфеты"

    candy = models.ForeignKey(
        Candy, 
        verbose_name="Конфета",
        on_delete=models.CASCADE, 
        null=False, 
        blank=True
    )
    order = models.ForeignKey(
        Order,
        verbose_name="Заказ",
        on_delete=models.CASCADE,
        null=False,
        blank=True
    )
    weight = models.PositiveSmallIntegerField(
        verbose_name="Вес в граммах",
        null=False,
        blank=True,
    )

    @property
    def price(self) -> float:
        return self.weight * self.candy.price / 100
    
    def __str__(self) -> str:
        return f"Заказ - {self.order.pk}, конфета - {self.candy.pk}"
