from django import forms
from .models import Product, Category,Review


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class ReviewForm(forms.ModelForm):
    body = forms.CharField(label="Review")

    class Meta:
        model = Review
        fields = ('body',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        body = forms.CharField(required=True)
        placeholders = {
            'body': 'What do you think of this product?',
        }