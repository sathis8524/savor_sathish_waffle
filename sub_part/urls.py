from django.urls import path
from django.contrib import admin
from django.urls import path
from sub_part import views   # ✅ app name use பண்ணு

from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('home',views.index,name='index'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('products',views.products,name='products'),
    path('buynow',views.buynow,name='buynow'),
    path('register_account_form_submission',views.register_account_form_submission,name='register_account_form_submission'),
    path('customer_login_from_submission',views.customer_login_from_submission,name='customer_login_from_submission'),
    path('buynow',views.buynow,name='buynow'),
    path('send-email', views.send_email, name='send_email'),
    path('save-order/',views.save_order),
]