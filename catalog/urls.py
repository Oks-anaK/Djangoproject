from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductTemplateView, ProductUnpublishView, CategoryDetail
from catalog.views import (
    ProductsListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
)

app_name = CatalogConfig.name

urlpatterns = [
    path("contacts/", ProductTemplateView.as_view(), name="products_contacts"),
    path("products/", ProductsListView.as_view(), name="products_list"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="products_detail"),
    path("products/create/", ProductCreateView.as_view(), name="products_create"),
    path(
        "products/<int:pk>/update/", ProductUpdateView.as_view(), name="products_update"
    ),
    path(
        "products/<int:pk>/delete/", ProductDeleteView.as_view(), name="products_delete"
    ),
    path(
        "product/<int:pk>/unpublish/",
        ProductUnpublishView.as_view(),
        name="product_unpublish",
    ),
    path(
        "products/category/<int:pk>/",
        CategoryDetail.as_view(),
        name="products_category",
    ),
]
