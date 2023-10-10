from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=10)
    email = models.EmailField(unique=True)
    contact_number = models.CharField(max_length=15)
    company = models.CharField(max_length=100, null=True, blank=True)
