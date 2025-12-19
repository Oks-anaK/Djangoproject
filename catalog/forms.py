from django.db.models import BooleanField
from django.forms import ModelForm
from django.core.exceptions import ValidationError

from catalog.models import Product

forbidden_words = [
    "казино",
    "криптовалюта",
    "крипта",
    "биржа",
    "дешево",
    "бесплатно",
    "обман",
    "полиция",
    "радар",
]


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control"


class ProductForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        exclude = ("view_counter",)

    def clean_name(self):
        name = self.cleaned_data.get("name")
        name_lower = name.lower()

        for word in forbidden_words:
            if word in name_lower:
                raise ValidationError("Выбранное вами слово запрещено для использования.")
        
        return name

    def clean_description(self):
        description = self.cleaned_data.get("description")
        description_lower = description.lower()

        for word in forbidden_words:
            if word in description_lower:
                raise ValidationError("Выбранное вами слово запрещено для использования.")
        
        return description

    def clean_price(self):
        price = self.cleaned_data.get("price")

        if price < 0:
            raise ValidationError("Цена продукта не может быть отрицательной.")
        return price
