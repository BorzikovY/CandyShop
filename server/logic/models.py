from django.db import models
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator
)
from logic.geolocation import generate_coordinates


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
    image = models.URLField(
        verbose_name="Изображение",
        null=True,
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
    weight = models.PositiveSmallIntegerField(
        verbose_name="Вес в граммах",
        null=False,
        blank=True,
    )

    @property
    def price(self) -> float:
        return self.weight * self.candy.price / 100

    def __str__(self) -> str:
        return f"{self.pk}, конфета - {self.candy.pk}"


class Order(models.Model):
    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    latitude = models.DecimalField(
        verbose_name="Широта",
        max_digits=10,
        decimal_places=8,
        default=round(generate_coordinates("Москва", 1)[0][0], 8),
    )
    longitude = models.DecimalField(
        verbose_name="Долгота",
        max_digits=11,
        decimal_places=8,
        default=round(generate_coordinates("Москва", 1)[0][1], 8),
    )
    date_time = models.DateTimeField(
        verbose_name="Дата заказа",
        auto_now_add=True
    )
    candies = models.ManyToManyField(
        OrderedCandy,
        verbose_name="Заказанные конфеты",
        blank=True
    )

    @property
    def price(self) -> float:
        return sum(
            ordered_candy.price
            for ordered_candy in self.candies.all()
        )

    def __str__(self) -> str:
        return str(self.date_time)


class Feedback(models.Model):
    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    author = models.CharField(
        verbose_name="Автор",
        max_length=32,
        null=False,
        blank=True
    )
    text = models.TextField(
        verbose_name="Текст отзыва",
        null=False,
        blank=True
    )
    date = models.DateField(
        verbose_name="Дата Создания",
        auto_now_add=True
    )
    stars = models.PositiveSmallIntegerField(
        verbose_name="Оценка",
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    def __str__(self) -> str:
        return self.author
