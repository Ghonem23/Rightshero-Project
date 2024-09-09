from django import forms
from .models import Category

class CategoryForm(forms.Form):
    categories = forms.ModelChoiceField(
        queryset=Category.objects.filter(parent__isnull=True),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )