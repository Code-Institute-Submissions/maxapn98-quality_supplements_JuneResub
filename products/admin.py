from django.contrib import admin
from .models import Product, Category

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'brand_name',
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


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)