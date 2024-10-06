from django.shortcuts import render

from .models import Contact
from apps.common.models import SubEmail


def contact(request):
    search = request.POST.get('search')

    if request.method == "POST":
        contact = Contact()

        contact.name = request.POST.get('name')
        contact.email = request.POST.get('email')
        contact.phone_number = request.POST.get('phone_number')
        contact.message = request.POST.get('message')

        contact.save()

    if request.method == "POST":
        sub_email = SubEmail()

        sub_email.sub_email = request.POST.get('sub_email')

        sub_email.save()

    return render(request=request, template_name='contact.html')
