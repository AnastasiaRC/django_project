from django import forms
from .models import Product, Version


class ProductForm(forms.ModelForm):
    prohibited_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                        'радар']

    class Meta:
        model = Product
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean_title_product(self):
        cleaned_data = self.cleaned_data['title_product'].lower()
        for word in self.prohibited_words:
            if word in cleaned_data:
                raise forms.ValidationError(f"Нельзя использовать в названии продукта слово: {word}")
        return cleaned_data

    def clean_description_product(self):
        cleaned_data = self.cleaned_data['description_product'].lower()
        for word in self.prohibited_words:
            if word in cleaned_data:
                raise forms.ValidationError(f"Нельзя использовать в описании продукта слово: {word}")
        return cleaned_data


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != 'is_active':
                field.widget.attrs['class'] = 'form-control'
