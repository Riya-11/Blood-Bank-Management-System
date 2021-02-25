from datetime import date
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.shortcuts import render
from django.urls import reverse
# from django import forms
from bloodcamp.forms import newdonor, newcamp
from . import forms
from .models import *
from .bloodcamps_functions import default_fun
from django.contrib import messages


# Create your views here.

def Volunteering(request):
    volunteerform = forms.VolunteerForm()
    if request.method == "POST":
        volunteerform = forms.VolunteerForm(data=request.POST)
        if volunteerform.is_valid():
            volunteerform.save()

            return HttpResponseRedirect(reverse('home:index'))
    return render(request, 'bloodcamp/volunteerform.html', {'volunteer': volunteerform})


def VolunteerList(request):
    obj = BloodVolunteer.objects.all()
    return render(request, 'bloodcamp/volunteer_list.html', {'volunteer': obj})



def index(request):
    return render(request, 'bloodcamp/index.html')


def camphome(request):
    return render(request, 'bloodcamp/camphome.html')




def history(request):
    default_fun(request)

    camps = BloodCamp.objects.filter(status='1')
    donors = BloodCampDonor.objects.all()

    for camp in camps:
        print(camp.campid)
        if donors:
            for donor in donors:
                if donor.bloodcamp.campid == camp.campid:
                    print(donor.firstname)

    content = {
        'camps': camps,
        'donors': donors,
    }
    return render(request, 'bloodcamp/history.html', context=content)


def ongoing(request):
    default_fun(request)

    camps = BloodCamp.objects.filter(status=2)
    donors = BloodCampDonor.objects.all()

    for camp in camps:
        print(camp.campid)
        if donors:
            for donor in donors:
                if donor.bloodcamp.campid == camp.campid:
                    print(donor.firstname)

    content = {
        'camps': camps,
        'donors': donors,
    }
    return render(request, 'bloodcamp/ongoing.html', context=content)


def upcoming(request):
    default_fun(request)

    camps = BloodCamp.objects.filter(status=3)
    donors = BloodCampDonor.objects.all()

    for camp in camps:
        print(camp.campid)
        if donors:
            for donor in donors:
                if donor.bloodcamp.campid == camp.campid:
                    print(donor.firstname)

    content = {
        'camps': camps,
        'donors': donors,
    }

    return render(request, 'bloodcamp/upcoming.html', context=content)


def newcamppage(request):
    form = newcamp()
    if request.method == 'POST':
        form = newcamp(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return camphome(request)
        else:
            print('form invalid')
    return render(request, 'bloodcamp/newcamp.html', {'form': form})


def newdonorpage(request):
    form1 = newdonor('3',request.POST)
    if request.method == 'POST':
        bdl=BloodCampDonor.objects.values_list('email', flat=True).filter(bloodcamp=request.POST['bloodcamp'])
        bdl=list(bdl)
        if form1.is_valid() and request.POST['email'] not in bdl:
            form1.save(commit=True)
            firstname = form1.cleaned_data['firstname']
            lastname = form1.cleaned_data['lastname']
            phone = form1.cleaned_data['phone']
            blood = form1.cleaned_data['blood']
            email = str(form1.cleaned_data['email'])
            bloodcamp = form1.cleaned_data['bloodcamp']
            startdate = bloodcamp.startdate
            enddate = bloodcamp.enddate
            send_mail(
                'Blood Bank',
                'FirstName:' + str(firstname) + '\n' +
                'Lastname:' + str(lastname) + '\n' +
                'Phone:' + str(phone) + '\n' +
                'Blood:' + str(blood) + '\n' +
                'startdate:' + str(startdate) + '\n' +
                'enddate:' + str(enddate) + '\n' +
                'Visit on these days to donate blood' + '\n' +
                'bloodcamp:' + str(bloodcamp) + '\n' ,
                '29riyajain@gmail.com',
                [email],
                fail_silently=False,
            )

            return camphome(request)
        else:
            messages.error(request, 'This Email already registered')
    return render(request, 'bloodcamp/newdonor.html', {'form1': form1})
