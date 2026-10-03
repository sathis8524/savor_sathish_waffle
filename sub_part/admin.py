from django.contrib import admin
from . models import customer_register_table, Order
# Register your models here.
# admin.site.register(customer_register_table)
# from .models import Order
# admin.site.register(Order)

class CustomerRegisterAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'email_id', 'phone_number', 'other_gender', 'password', 'register_dt')
    search_fields= ('full_name', 'email_id', 'phone_number')
    list_per_page= 100

admin.site.register(customer_register_table, CustomerRegisterAdmin)
admin.site.register(Order)    