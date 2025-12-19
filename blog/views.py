from blog.forms import PostForm
from blog.models import Post
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView,
)
from django.urls import reverse_lazy, reverse


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(published_is=True)


class PostDetailView(DetailView):
    model = Post

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_counter += 1
        self.object.save()
        return self.object


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy("blog:posts_list")


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy("blog:posts_list")

    def get_success_url(self):
        return reverse("blog:posts_detail", args=[self.kwargs.get("pk")])


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy("blog:posts_list")


class PostTemplateView(TemplateView):
    template_name = "blog/post_contacts.html"

    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        # Обработка данных
        context = self.get_context_data()
        context["success_message"] = f"Спасибо, {name}! Ваш номер и сообщение получено."
        return self.render_to_response(context)
