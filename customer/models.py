from django.db import models
# Create your models here.


class Customer(models.Model):
    class CustomerType(models.TextChoices):
        REGULAR = "Regular", "Regular"
        VIP = "VIP", "VIP"

    name = models.CharField(max_length=50, unique=True)
    customer_type = models.CharField(choices=CustomerType, max_length=15)
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    phone = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['name']
        # app_label = 'customer'

    def __str__(self):
        return self.name