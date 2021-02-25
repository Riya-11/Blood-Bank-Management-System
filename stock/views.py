from django.shortcuts import render
from .models import BloodAvailability
from home.models import UserAddress
from django.core.mail import send_mail


# Create your views here.


# This function is only for generating the availability list
def index(request):
    availability = BloodAvailability.objects.all()
    Availability = {'available': availability}

    return render(request, "stock/index.html", context=Availability)


# This function generates array of emails needed to be notified
# and accessing the userdata for checking his bloodgroup


def sendingmail(request):
    Availability = BloodAvailability.objects.all()
    for availability in Availability:
        if availability.bloodgroup_A_minus < availability.threshhold:
            a_minus = 'A-'
            Donor_data_selected = UserAddress.objects.filter(blood=a_minus)
            for user in Donor_data_selected:
                Email_List = [user.user.email,]
        if availability.bloodgroup_A_plus < availability.threshhold:
            a_minus = 'A+'
            Donor_data_selected = UserAddress.objects.filter(blood=a_minus)
            for user in Donor_data_selected:
                Email_List = [user.user.email,]
        if availability.bloodgroup_B_minus < availability.threshhold:
            a_minus = 'B-'
            Donor_data_selected = UserAddress.objects.filter(blood=a_minus)
            for user in Donor_data_selected:
                Email_List = [user.user.email,]
        if availability.bloodgroup_B_plus < availability.threshhold:
            a_minus = 'B+'
            Donor_data_selected = UserAddress.objects.filter(blood=a_minus)
            for user in Donor_data_selected:
                Email_List = [user.user.email,]
        if availability.bloodgroup_AB_minus < availability.threshhold:
            a_minus = 'AB-'
            Donor_data_selected = UserAddress.objects.filter(blood=a_minus)
            for user in Donor_data_selected:
                Email_List = [user.user.email,]
        if availability.bloodgroup_AB_plus < availability.threshhold:
            a_minus = 'A-'
            Donor_data_selected = UserAddress.objects.filter(blood=a_minus)
            for user in Donor_data_selected:
                Email_List = [user.user.email,]
        if availability.bloodgroup_O_minus < availability.threshhold:
            a_minus = 'O-'
            Donor_data_selected = UserAddress.objects.filter(blood=a_minus)
            for user in Donor_data_selected:
                Email_List = [user.user.email,]
        if availability.bloodgroup_O_plus < availability.threshhold:
            a_minus = 'O+'
            Donor_data_selected = UserAddress.objects.filter(blood=a_minus)
            for user in Donor_data_selected:
                Email_List = [user.user.email,]

        send_mail(
            'Notification regarding low blood availability in bloodbank',
            'This is to be notified that low blood availability your presence is required ',
            'vedavyas22541@gmail.com',
            Email_List,
        )
    return render(request, "stock/mail.html")
