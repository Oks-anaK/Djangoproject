from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.core.exceptions import PermissionDenied

from catalog.models import Product
from catalog.forms import ProductForm
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView,
)
from django.urls import reverse_lazy, reverse


class ProductTemplateView(TemplateView):
    template_name = "catalog/product_contacts.html"

    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        # Обработка данных
        context = self.get_context_data()
        context["success_message"] = f"Спасибо, {name}! Ваше сообщение получено."
        return self.render_to_response(context)


class ProductsListView(ListView):
    model = Product


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_counter += 1
        self.object.save()
        return self.object


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:products_list")

    def form_valid(self, form):
        # Устанавливаем владельца продукта текущим пользователем
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:products_list")

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()

        # Проверяем, что пользователь является владельцем
        if self.object.owner != request.user:
            raise PermissionDenied("Вы не можете редактировать этот продукт.")

        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("catalog:products_detail", args=[self.kwargs.get("pk")])


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:products_list")

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()

        # Проверяем: владелец ИЛИ модератор
        is_owner = self.object.owner == request.user
        is_moderator = request.user.has_perm('catalog.delete_product')

        if not (is_owner or is_moderator):
            from django.core.exceptions import PermissionDenied
            raise PermissionDenied("У вас нет прав для удаления этого продукта")

        return super().dispatch(request, *args, **kwargs)


class ProductUnpublishView(PermissionRequiredMixin, LoginRequiredMixin, UpdateView):
    model = Product
    permission_required = 'catalog.can_unpublish_product'
    success_url = reverse_lazy('catalog:products_list')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        self.object.published_is = False

        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
