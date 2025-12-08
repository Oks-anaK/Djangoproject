from django.urls import path
from blog.apps import BlogConfig
from blog.views import (
    PostListView,
    PostCreateView,
    PostDetailView,
    PostUpdateView,
    PostDeleteView,
    PostTemplateView,
)

app_name = BlogConfig.name

urlpatterns = [
    path("posts/", PostListView.as_view(), name="posts_list"),
    path("posts/<int:pk>/", PostDetailView.as_view(), name="posts_detail"),
    path("posts/create/", PostCreateView.as_view(), name="posts_create"),
    path("posts/<int:pk>/update/", PostUpdateView.as_view(), name="posts_update"),
    path("posts/<int:pk>/delete/", PostDeleteView.as_view(), name="posts_delete"),
    path("posts/contacts/", PostTemplateView.as_view(), name="posts_contacts"),
]
