from django.db import models

# Create your models here.

class Message(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    message = models.TextField(max_length=300)