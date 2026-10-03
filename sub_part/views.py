from django.shortcuts import render
from . models import*
import datetime
from django.contrib import messages

from django.contrib import messages

from django.core.mail import send_mail
from django.conf import settings

from django.http import HttpResponse
from django.core.mail import send_mail

from django.http import JsonResponse
from.models import Order              #save order logic
# Create your views here.
def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def products(request):
    return render(request,'products.html')

def buynow(request):
    return render(request,'buynow.html')

def register_account_form_submission(request):
    
    if request.method=="POST":
        print("data received")
        full_name = request.POST.get('full_name')
        print(f"full name is {full_name}")
        email_id = request.POST.get('email_id')
        print(f"email id is {email_id}")
        phone_number = request.POST.get('phone_number')
        print(f"phone number is {phone_number}")
        other_gender = request.POST.get('other_gender')
        print(f"gender is {other_gender}")
        password = request.POST.get('password')
        print(f"password is {password}")

        # date time logic
        date_time = datetime.datetime.now()
        print(f"register time {date_time}")

        # 1. Validation (Email / Phone ஏற்கனவே உள்ளதா எனச் சரிபார்ப்பது)
        if customer_register_table.objects.filter(email_id=email_id, phone_number=phone_number).exists():
            print("already this email and phone number has registered")
            messages.error(request, 'already this email and phone number has registered', extra_tags='already')
            return render(request, "register.html")

        elif customer_register_table.objects.filter(email_id=email_id).exists():
            print("already this email has registered")
            messages.error(request, 'already this email has registered', extra_tags='already')
            return render(request, "register.html")

        elif customer_register_table.objects.filter(phone_number=phone_number).exists():
            print("already this phone number has registered")
            messages.error(request, 'already this phone number has registered', extra_tags='already')
            return render(request, "register.html")

        else:
            # 2. Database-ல் புதிய பயனரைச் சேமிப்பது
            ex1 = customer_register_table(
                full_name=full_name,
                email_id=email_id,
                phone_number=phone_number,
                other_gender=other_gender,
                password=password,
                register_dt=date_time
            )
            ex1.save()
            print("***data saved successfully")

            # 3. Email அனுப்பும் பகுதி (fail_silently=True உடன்)
            try:
                subject = "welcome to chocolate world"
                message = f'hello...{full_name}, your registration successful'
                send_mail(
                    subject, 
                    message, 
                    settings.EMAIL_HOST_USER, 
                    [email_id],
                    fail_silently=False  # Email அனுப்ப முடியாவிட்டாலும் Error தூக்காது!
                )
                print('Email sent successfully')
            except Exception as e:
                print('Email not sent:', e)

            # 4. பதிவு முடிந்ததும் லாகின் பக்கத்திற்கு அனுப்புவது
            return render(request, 'login.html')

    else:
        print("data not received")
        return render(request, "register.html")
    
    
def customer_login_from_submission(request):
    if customer_register_table.objects.filter(email_id=request.POST.get('email_id'),password=request.POST.get('password')):
        print("login successfully")
        return render(request,'products.html')
    else:
        print("check your email or password")
        messages.error(request,'check email or password ',extra_tags='failed')
        return render(request,'login.html')
# buynow logic
def buynow(request):
    name = request.GET.get('name')
    price = request.GET.get('price')
    img = request.GET.get('img')

    context = {
        'name': name,
        'price': price,
        'img': img
    }

    return render(request, 'buynow.html', context)
# buynow email send logic
def send_email(request):
    email = request.GET.get('email')
    name = request.GET.get('name')

    send_mail(
        'Order Confirmation',
        f'Thank you {name} for your order!',
        'your_email@gmail.com',
        [email],
        fail_silently=False,
    )

    return HttpResponse("Email sent successfully")
  

def save_order(request):
    if request.method=="POST":
       name=request.POST.get('name')
       price=request.POST.get('price')
       qty=request.POST.get('qty')
       total=request.POST.get('total')
       address=request.POST.get('address')
       email=request.POST.get('email')

       Order.objects.create(product_name=name,
                            price=price,
                            quantity=qty,
                            total_amount=total,
                            address=address,
                            email=email)
       
       return JsonResponse({"status":"success"})
       return JsonResponse({"status": "failed"})