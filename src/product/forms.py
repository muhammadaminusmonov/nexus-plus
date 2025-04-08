from django import forms
from .models import Product
from category.models import Category, Brand
from region.models import Region


class AddProductForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add your title'})
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control input-md', 'placeholder': 'Add your description'})
    )

    location = forms.ModelChoiceField(queryset=Region.objects.all(), widget=forms.Select(
        attrs={'class': 'tg-select form-control', 'label': 'Select location'}))

    category = forms.ModelChoiceField(queryset=Category.objects.filter(is_main=True), widget=forms.Select(attrs={'class': 'tg-select form-control', 'label': 'Select category'}))

    brand = forms.ModelChoiceField(queryset=Brand.objects.all(), widget=forms.Select(attrs={'class': 'tg-select form-control', 'label': 'Select brand'}))

    condition = forms.ChoiceField(choices=Product.condition_types, widget=forms.Select(attrs={'class': 'tg-select form-control', 'label': 'Select condition'}))

    price = forms.IntegerField(
        widget=forms.NumberInput(attrs={'class': 'form-control input-md', 'placeholder': 'Add your price'})
    )

    slug = forms.SlugField(
        widget=forms.TextInput(attrs={'class': 'form-control input-md', 'placeholder': 'Add your slug', 'label': 'slug'})
    )

    featured = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'custom-control-input', 'id': 'tg-priceoncall'}))

    discount = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'class': 'form-control input-md', 'placeholder': 'Add your discount'}))

    class Meta:
        model = Product
        exclude = ['user', 'status', 'review', 'created_at', 'updated_at']
