from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'


    product_category = models.CharField(max_length=254) #update

    def __str__(self):
        return self.product_category



class Product(models.Model):
    product_category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    brand_name = models.CharField(max_length=254, null=True, blank=True)
    product_name = models.CharField(max_length=254)
    product_description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    

    def __str__(self):
        return self.product_name


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user =  models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(max_length=500, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.user.username