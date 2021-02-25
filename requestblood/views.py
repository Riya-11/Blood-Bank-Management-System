from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.template.loader import render_to_string
from .forms import RequestorForm
from .models import Requestor
from home.models import *
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from datetime import date


# Create your views here.

def index(request, req_blood):
    current_site = get_current_site(request)
    if request.method == 'POST':
        form = RequestorForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            reason = form.cleaned_data['reason']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']

            # blood = request.POST.get('blood')
            blood =req_blood
            print(blood)

            if UserAddress.objects.filter(blood=blood, city=city, state=state, ).count() == 0:
                return render(request, 'requestblood/sorry.html', {'error': 'Sorry.no donor found near you!'})

            print(date.today())
            print(date)
            # print(Requestor.objects.filter(name=name, phone=phone, date=date.today()))
            if Requestor.objects.filter(name=name, phone=phone, date=date.today(), blood=blood).exists():
                return render(request, 'requestblood/sorry.html',
                              {'error': 'Your request has already been sent. Please wait for donor\'s response'})

            else:
                requestor = Requestor.objects.create(name=name, blood=blood, phone=phone, email=email, reason=reason,
                                                     state=state, city=city)

                query = UserAddress.objects.filter(blood=blood, city=city)
                result = UserAddress.objects.none()

                for donor in query:
                    a = UserHistory.objects.filter(user=donor.user)
                    recent = a.count() - 1

                    b = UserAddress.objects.get(user=a[0].user)
                    if a[recent].donation_date and (datetime.date.today()-b.birth).days > 6570:
                        if (datetime.date.today() - a[recent].donation_date.date()).days > 90:
                            result |= a
                subject = 'Request for blood'
                print(result)

                from_email = requestor.email

                for donor in result:

                    to_email = [donor.user.email, ]
                    link = 'http://' + current_site.domain + '/donate/'

                    context = {
                        'link': link,
                        'username': donor.user.username,
                        'requestor': requestor.name,
                        'reason': requestor.reason,
                        'phone': requestor.phone,
                        'email': requestor.email,

                    }
                    message = render_to_string('requestblood/email.html', context)
                    msg = EmailMessage(subject, message, to=[to_email], from_email=from_email)
                    msg.content_subtype = 'html'

                    try:

                        msg.send()
                        print('Successful')
                    except:
                        print('\nUnsuccessful attempt')
                        return render(request, 'requestblood/sorry.html',
                                      {'error': 'There was an error in sending the email'})

                return render(request, 'requestblood/response.html')

    else:
        form = RequestorForm()

    return render(request, 'requestblood/index.html', {'form': form, 'blood': req_blood})


def sorry(request):
    return render(request, 'requestblood/sorry.html')


def response(request):
    return render(request, 'requestblood/response.html')


def redi(request):
    return redirect('availability:index')
