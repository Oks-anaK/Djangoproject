from django.db import models


class Post(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name="Заголовок",
        help_text="Введите заголовок поста.",
    )
    content = models.TextField(
        verbose_name="Содержимое поста", help_text="Введите содержимое поста."
    )
    preview = models.ImageField(
        upload_to="catalog/preview",
        blank=True,
        null=True,
        verbose_name="Изображение поста",
        help_text="Добавьте изображение для поста.",
    )
    created_at = models.DateField(
        blank=True,
        null=True,
        verbose_name="Дата создания поста",
        help_text="Добавьте дату создания поста.",
    )
    published_is = models.BooleanField(
        default=False,
        blank=True,
        verbose_name="Опубликовано",
        help_text="Отметьте, если пост опубликован",
    )
    view_counter = models.PositiveIntegerField(
        default=0,
        verbose_name="Счетчик просмотров поста",
        help_text="Укажите количество просмотров поста.",
    )

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ["title", "created_at", "published_is", "view_counter"]

    def __str__(self):
        return self.title
