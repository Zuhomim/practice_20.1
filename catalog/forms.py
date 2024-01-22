from django import forms

from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    excluded_list = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

    class Meta:
        model = Product
        fields = '__all__'

        permissions = [
            (
                'set_is_published',
                'Can change is_published'
            ),
            (
                'set_description',
                'Can change description'
            ),
            (
                'set_category',
                'Can change category'
            )
        ]

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        for item in self.excluded_list:
            if item in cleaned_data:
                raise forms.ValidationError('Ошибка, связанная с недопустимым названием')
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        for item in self.excluded_list:
            if item in cleaned_data:
                raise forms.ValidationError('Ошибка, связанная с недопустимым описанием')
        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Version
        fields = '__all__'


class ProductFormModerator(StyleFormMixin, forms.ModelForm):

    excluded_list = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

    class Meta:
        model = Product
        fields = ('description', 'category', 'is_published',)

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        for item in self.excluded_list:
            if item in cleaned_data:
                raise forms.ValidationError('Ошибка, связанная с недопустимым названием')
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        for item in self.excluded_list:
            if item in cleaned_data:
                raise forms.ValidationError('Ошибка, связанная с недопустимым описанием')
        return cleaned_data
