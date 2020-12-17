from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render
from django.http import HttpResponse

from .forms import ContactForm

def contact(request):
    return render(request, 'contact/contact.html')
