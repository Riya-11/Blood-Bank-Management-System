from django.shortcuts import render
from .models import Hospital


def hospitals(request):
    hospitals = Hospital.objects.all()
    context = {'hospitals': hospitals, }
    return render(request, 'Hospitals/index.html', context)



