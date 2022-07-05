from django import forms
from .models import Product, Category,Review


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()


class ReviewForm(forms.ModelForm):
    body = forms.CharField(label="Review", widget=forms.Textarea(attrs={
        "rows": 4,
        "cols": 50,
    }))

    class Meta:
        model = Review
        fields = ('body',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)