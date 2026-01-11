from django.db import models

from users.models import User


class Product(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование товара",
        help_text="Введите наименование товара.",
    )
    description = models.TextField(
        verbose_name="Описание товара", help_text="Введите описание товара."
    )
    image = models.ImageField(
        upload_to="catalog/photo",
        blank=True,
        null=True,
        verbose_name="Изображение товара",
        help_text="Добавьте изображение товара.",
    )
    category = models.ForeignKey(
        "Category",
        on_delete=models.SET_NULL,
        verbose_name="Категория товара",
        help_text="Введите категорию товара.",
        blank=True,
        null=True,
        related_name="products",
    )
    price = models.IntegerField(
        verbose_name="Цена товара", help_text="Введите стоимость товара."
    )

    delivery_option_is = models.BooleanField(
        verbose_name="Возможность доставки",
        help_text="Отметьте галочкой, если есть возможность доставки товара.",
        default=False,
    )
    created_at = models.DateField(
        blank=True,
        null=True,
        verbose_name="Дата создания товара",
        help_text="Добавьте дату создания товара.",
    )
    updated_at = models.DateField(
        blank=True,
        null=True,
        verbose_name="Дата последнего изменения товара",
        help_text="Добавьте дату последнего изменения товара.",
    )
    view_counter = models.PositiveIntegerField(
        verbose_name="Счетчик просмотров",
        help_text="Укажите количество просмотров.",
        default=0,
    )
    published_is = models.BooleanField(
        default=False,
        blank=True,
        verbose_name="Опубликовано",
        help_text="Отметьте, если нужно опубликовать",
    )
    owner = models.ForeignKey(
        User,
        verbose_name="Владелец",
        help_text="Укажите владельца продукта",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name = 'products',
    )

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ["name", "category", "price", "created_at", "updated_at"]
        permissions = [
            ("can_unpublish_product", "Can unpublish product"),
        ]

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование категории",
        help_text="Введите наименование категории товаров.",
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание категории",
        help_text="Введите описание категории товаров.",
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = [
            "name",
        ]

    def __str__(self):
        return self.name
