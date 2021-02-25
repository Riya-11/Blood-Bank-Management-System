import datetime

from django.shortcuts import render
from home.models import UserAddress, UserHistory
from .forms import BloodForm
from home.models import *
from django.http import HttpResponseRedirect, HttpResponse


def load_cities(request):
    # print("sdhksdsknsl")
    try:
        state_id = request.POST.get('state')
        cities = City.objects.filter(state_id=state_id).order_by('name')

    except:
        cities = City.objects.none()


    #print(state_id)

    # print(cities)
    return render(request, 'finddonor/dropdown.html', {'cities': cities})


def index(request):
    sorry = ''
    result = ''
    if request.method == 'POST':
        form = BloodForm(request.POST)

        if form.is_valid():
            blood = form.cleaned_data['blood']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            result = UserAddress.objects.filter(blood=blood, city=city, state=state)
            queryset = UserAddress.objects.none()
            # print(result)
            for donor in result:
                a = UserHistory.objects.filter(user=donor.user)
                recent = a.count()-1
                # print(a[0].donation_date)

                b = UserAddress.objects.get(user=a[0].user)
                print((datetime.date.today()-b.birth).days)
                if a[recent].donation_date and (datetime.date.today()-b.birth).days > 6570:
                    if (datetime.date.today() - a[recent].donation_date.date()).days > 90:
                        queryset |= UserAddress.objects.filter(user=donor.user)

            print(queryset)
            context = {'result': queryset, 'form': form, 'show': True}
            return render(request, 'finddonor/index.html', context)

    else:
        form = BloodForm()

    return render(request, 'finddonor/index.html', {'form': form, 'show': False})
