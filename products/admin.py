from django.contrib import admin
from .models import Product, Category, Review

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'brand_name',
        'sku',
        'product_name',
        'product_category',
        'price',
        'rating',
        'image',
    )

    ordering = ('brand_name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'product_category',
    )



admin.site.register(Review)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)