from django.urls import path, include
from catalog.apps import CatalogConfig
from catalog.views import home
from catalog.views import contacts
from catalog.views import answer


app_name = CatalogConfig.name

urlpatterns = [
    path('home/', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('answer/', answer, name='answer')
]
