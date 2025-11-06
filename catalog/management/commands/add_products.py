from django.core.management.base import BaseCommand
from catalog.models import Product, Category
from django.db import transaction


class Command(BaseCommand):
    help = (
        "Adds products with their categories. Creates categories if they don't exist."
    )

    @transaction.atomic  # Гарантия, что все операции пройдут успешно или ни одна
    def handle(self, *args, **options):

        # --- Создание или получение категорий ---
        category_chancery, created_cat1 = Category.objects.get_or_create(
            name="Канцелярия",
            defaults={"description": "Все, что можно купить в канцтоваром магазине."},
        )
        if created_cat1:
            self.stdout.write(
                self.style.SUCCESS(f"Создана категория: '{category_chancery.name}'")
            )
        else:
            self.stdout.write(
                self.style.WARNING(
                    f"Категория '{category_chancery.name}' уже существует."
                )
            )

        category_books, created_cat2 = Category.objects.get_or_create(
            name="Книги",
            defaults={"description": "Художественная и научная литература."},
        )
        if created_cat2:
            self.stdout.write(
                self.style.SUCCESS(f"Создана категория: '{category_books.name}'")
            )
        else:
            self.stdout.write(
                self.style.WARNING(f"Категория '{category_books.name}' уже существует.")
            )

        category_sport, created_cat3 = Category.objects.get_or_create(
            name="Спорт", defaults={"description": "Товары для спорта."}
        )
        if created_cat3:
            self.stdout.write(
                self.style.SUCCESS(f"Создана категория: '{category_sport.name}'")
            )
        else:
            self.stdout.write(
                self.style.WARNING(f"Категория '{category_sport.name}' уже существует.")
            )

        # --- Данные для продуктов ---
        products_data = [
            {
                "name": "Ручка синяя",
                "description": "Классическая синяя ручка.",
                "price": 50,
                "category": category_chancery,
            },
            {
                "name": "Карандаш HB",
                "description": "Стандартный карандаш.",
                "price": 20,
                "category": category_chancery,
            },
            {
                "name": "Коврик для фитнеса",
                "description": "Синий износостойский коврик для йоги и фитнеса.",
                "price": 1500,
                "category": category_sport,
            },
            {
                "name": 'Книга "Мастер и Маргарита"',
                "description": "Знаменитый роман Михаила Булгакова.",
                "price": 700,
                "category": category_books,
            },
            {
                "name": 'Книга "1984"',
                "description": "Антиутопический роман Джорджа Оруэлла.",
                "price": 650,
                "category": category_books,
            },
            # Добавьте больше продуктов по необходимости
        ]

        # --- Итерация и добавление продуктов ---
        for product_data in products_data:

            product, created = Product.objects.get_or_create(
                name=product_data["name"],  # Поле для поиска дубликатов
                defaults={
                    "description": product_data["description"],
                    "price": product_data["price"],
                    "category": product_data["category"],  # Ссылка на объект Category
                },
            )

            if created:
                self.stdout.write(
                    self.style.SUCCESS(f"Успешно добавлен продукт: '{product.name}'")
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f"Продукт '{product.name}' уже существует.")
                )
