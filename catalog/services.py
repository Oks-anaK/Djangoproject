from catalog.models import Product, Category
from config.settings import CACHE_ENABLED
from django.core.cache import cache

from users.models import User


def get_products_from_cache():
    """Получает данные о продуктах из кеша, если кеш пуст, получает данные из БД."""
    if not CACHE_ENABLED:
        return Product.objects.all()

    products = cache.get("products_queryset")

    if not products:
        products = Product.objects.all()
        cache.set("products_queryset", products, 60 * 15)

    return products


def sorting_products_by_category(category_name):
    """Возвращает список товаров в указанной категории с кешированием."""
    if not CACHE_ENABLED:
        return Product.objects.filter(category__name=category_name)

    cache_key = f"products_category_{category_name}"
    products = cache.get(cache_key)

    if not products:
        products = Product.objects.filter(category__name=category_name)
        cache.set(cache_key, products, 60 * 15)

    return products
