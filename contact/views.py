from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render
from django.http import HttpResponse

def contact(request):
    return render(request, 'contact/contact.html')
