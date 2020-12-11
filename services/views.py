from django.shortcuts import render

from .models import Service

# Create your views here.
def services_main_view(request):
    context = {
        'service_list': Service.objects.all()
    }
    return render(request, 'services/services_list.html', context)
