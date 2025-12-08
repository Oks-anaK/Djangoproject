from django.contrib import admin
from blog.models import Post


@admin.register(Post)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "published_is")
    list_filter = ("published_is",)
    search_fields = ("name", "published_is")
