from django.db import models
from django.utils import timezone

# Create your models here.

class customer_register_table(models.Model):
    full_name=models.CharField(max_length=100)
    email_id=models.CharField(max_length=255)
    phone_number=models.CharField(max_length=15)
    other_gender=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    register_dt=models.CharField(max_length=100)

class Order(models.Model):
    product_name=models.CharField(max_length=100)
    price=models.IntegerField()
    quantity=models.IntegerField()
    total_amount=models.IntegerField()
    address=models.TextField()
    email=models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)


