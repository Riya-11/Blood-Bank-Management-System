from django.shortcuts import render
from .models import BloodAvailability



# Create your views here.

def index(request):
    quantity = BloodAvailability.objects.all()
    context = {
        'quantity': quantity
    }
    return render(request, 'availability/index.html', context)


