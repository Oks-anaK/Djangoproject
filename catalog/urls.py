from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import contacts
from catalog.views import answer
from catalog.views import products_list
from catalog.views import products_detail

app_name = CatalogConfig.name

urlpatterns = [
    path("contacts/", contacts, name="contacts"),
    path("answer/", answer, name="answer"),
    path("products/", products_list, name="products_list"),
    path("products/<int:pk>/", products_detail, name="products_detail")
]
