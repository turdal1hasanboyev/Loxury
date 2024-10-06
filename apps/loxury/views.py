from django.shortcuts import render

from .models import Loxury
from apps.common.models import SubEmail
from apps.contact.models import Contact


def shop(request):
    search = request.POST.get('search')

    if request.method == 'POST':
        sub_email = request.POST.get('sub_email')

        SubEmail.objects.create(
            sub_email=sub_email,
        )
    
    loxury = Loxury.objects.filter(is_active=True).order_by('-id')

    if search:
        loxury = Loxury.objects.filter(is_active=True, name__icontains=search).order_by('-id')

    return render(request, 'shop.html', {'loxury': loxury[:6]})

def jewellery(request):
    search = request.POST.get('search')

    if request.method == 'POST':
        sub_email = request.POST.get('sub_email')

        SubEmail.objects.create(
            sub_email=sub_email,
        )

    return render(request=request, template_name='jewellery.html')

def about(request):
    search = request.POST.get('search')

    if request.method == 'POST':
        sub_email = SubEmail()

        sub_email.sub_email = request.POST.get('sub_email')

        sub_email.save()

    return render(request=request, template_name='about.html')

def home(request):
    search = request.POST.get('search')

    if request.method == 'POST':
        sub_email = request.POST.get('sub_email')

        SubEmail.objects.create(
            sub_email=sub_email,
        )

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        message = request.POST.get('message')
        
        Contact.objects.create(
            name=name,
            email=email,
            phone_number=phone_number,
            message=message,
        )

    loxury = Loxury.objects.filter(is_active=True).order_by('-id')

    if search:
        loxury = Loxury.objects.filter(is_active=True, name__icontains=search).order_by('-id')

    return render(request, 'index.html', {'loxury': loxury[:6]})
