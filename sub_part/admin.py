from django.contrib import admin
from . models import *
# Register your models here.
admin.site.register(customer_register_table)
from .models import Order
admin.site.register(Order)