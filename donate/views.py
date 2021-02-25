from django.core.mail import EmailMessage

from django.shortcuts import render, redirect
from django.contrib.sites.shortcuts import get_current_site
from .forms import AppointmentForm
from .forms import AppointmentForm
from .models import Appointment
from django.contrib.auth.decorators import login_required
from . import ref
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.conf import settings


# Create your views here.


@login_required(login_url='home:login')
def index(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)

        if form.is_valid():
            date = form.cleaned_data['date']
            pathlab = form.cleaned_data['date']
            time = form.cleaned_data['time']
            refno = ref.generate_app_id()
            donor = request.user
            print(donor.id)
            a = Appointment.objects.create(date=date, pathlab=pathlab, time=time, reference_no=refno, user=donor)

            subject = "Appointment booked"
            to_email = request.user.email
            print(to_email)
            context = {
                'name': donor.username,
                'reference':refno,
                'time':time,
                'date': date,
            }
            message = render_to_string('donate/email.html', context)
            msg = EmailMessage(subject, message, to=[to_email])
            msg.content_subtype = 'html'

            try:
                msg.send()
                print('Successful')
            except:
                print('Unsuccessful')

            return redirect('donate:thanks')

    else:
        form = AppointmentForm()

    return render(request, 'donate/index.html', {'form': form})


def thanks(request):
    return render(request, 'donate/thanks.html')
