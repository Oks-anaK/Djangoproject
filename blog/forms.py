from django.db.models import BooleanField
from django.forms import ModelForm
from django.core.exceptions import ValidationError

from blog.models import Post

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

                # Используем help_text как placeholder для текстовых полей
                if field.help_text:
                    field.widget.attrs["placeholder"] = field.help_text
                    field.help_text = ""


class PostForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Post
        exclude = ("view_counter", "published_is")

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title").lower()
        content = cleaned_data.get("content").lower()

        for word in forbidden_words:
            if word in title:
                self.add_error(
                    "title", "Выбранное вами слово запрещено для использования."
                )

        for word in forbidden_words:
            if word in content:
                self.add_error(
                    "content", "Выбранное вами слово запрещено для использования."
                )

    def clean_preview(self):
        preview = self.cleaned_data.get("preview")
        
        if preview:

            allowed_formats = ['image/jpeg', 'image/jpg', 'image/png']
            if preview.content_type not in allowed_formats:
                raise ValidationError(
                    "Формат изображения должен быть JPEG или PNG."
                )

            max_size = 5 * 1024 * 1024  # 5 МБ в байтах
            if preview.size > max_size:
                raise ValidationError(
                    "Размер изображения не должен превышать 5 МБ."
                )
        
        return preview
