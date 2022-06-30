from django.db import models

# Create your models here.


class Message(models.Model):
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    subject = models.CharField(
        max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    message = models.TextField(max_length=300, null=False, blank=False)

    def __str__(self):
        return f'Subject: {self.subject} Email: {self.email}'