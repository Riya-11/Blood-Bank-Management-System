from .models import *
from . import forms
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from credits.models import Wallet
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import send_mail, EmailMessage
import datetime


from django.contrib.auth import (
    update_session_auth_hash,
)
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponseRedirect, QueryDict
from django.utils.http import is_safe_url, urlsafe_base64_decode
from django.contrib import messages


def load_cities(request):
    try:
        state_id = request.POST.get('state')
        cities = City.objects.filter(state_id=state_id).order_by('name')

    except:
        cities = City.objects.none()

    return render(request, 'home/dropdown.html', {'cities': cities})

def index(request):
    return render(request,'home/index.html')

def faq(request):
    return render(request,'home/faq.html')
def readmore(request):
    return render(request,'home/readmore.html')
def SignUp(request):

    userform=forms.UserForm()
    useraddressform=forms.UserAddressForm()
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("home:profile"))

    if request.method=="POST":
        userform=forms.UserForm(data = request.POST)
        useraddressform=forms.UserAddressForm(data = request.POST)
        #birth = request.POST['birth']
        #if (datetime.date.today() - birth.date()).days < 365*18 :
        #    messages.error(request, 'You must be above 18 to donate blood')


        if userform.is_valid() and useraddressform.is_valid():
            user=userform.save(commit=False)
            try:
                obj = User.objects.get(email=user.email)
                #print("pahle",obj)
            except:
                obj=False
            if not obj:
                useraddress=useraddressform.save(commit=False)
                user.set_password(user.password)
                user.is_active = False
                user.save()
                useraddress.user=user
                #useraddress.birth=birth
                useraddress.save()


                UserProfile.objects.create(user = user)
                Wallet.objects.create(user = user)
                UserHistory.objects.create(user = user)
                current_site = get_current_site(request)
                subject = 'Activate Your BloodBank Account'
                message = render_to_string('home/account_activation_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)).decode(),
                    'token': account_activation_token.make_token(user),
                })
                #user.email_user(subject, message)
                to_email = userform.cleaned_data.get('email')
                email = EmailMessage(
                    subject, message, to=[to_email]
                )
                email.send()

                return HttpResponseRedirect(reverse('home:account_activation_sent'))
            messages.error(request, 'This Email already exists')
            #raise Http404("Email already exists")
        else:
            messages.error(request, 'Either Phone no. is not correct or This username already exists')

    return render(request,'home/signup.html',{'form':userform,'address':useraddressform})



def account_activation_sent(request):
    return render(request, 'home/account_activation_sent.html')




def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return HttpResponseRedirect(reverse('home:login'))
    else:
        return render(request, 'home/account_activation_invalid.html')



@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home:index'))



def LogIn(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("home:profile"))

    elif request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            #print("user")
            if user.is_active:
                #print("active")
                login(request, user)
                if 'next' in request.POST:
                    try:
                         return redirect(request.POST.get('next'))
                    except:
                        print('Next not found')

                return HttpResponseRedirect(reverse("home:index"))
            #print("yes")
            messages.error(request, 'This user does not exist')
            #return HttpResponseRedirect(reverse("home:login"))

        else:
            print("else")
            messages.error(request, 'username or password does not match')


    return render(request,'home/login.html',)


def about(request):
    return render(request,'home/about.html',)

@login_required
def profile(request):
    return render(request,'home/profile.html',)


@login_required
def Image_Upload(request):
    try:
        userprofile = request.user.userprofile
    except:
        return HttpResponseRedirect(reverse('home:profile'))

    imageform = forms.Upload_Image(instance = userprofile)

    if request.method == "POST":
        imageform = forms.Upload_Image(request.POST, request.FILES, instance = userprofile)

        if imageform.is_valid():

            imageform.save()
            #print("image name is ",x.image)

            return HttpResponseRedirect(reverse('home:profile'))
    return render(request,'home/uploadedpic.html',{'image':imageform})


@login_required
def Update_Details(request):
    userform = forms.UpdateUser(instance = request.user)
    try:
        addressform = forms.UploadAddress(instance = request.user.useraddress)
    except:
        return HttpResponseRedirect(reverse('home:profile'))

    if request.method == "POST":
        addressform = forms.UploadAddress(data = request.POST,instance = request.user.useraddress)
        userform = forms.UpdateUser(data = request.POST, instance = request.user)

        if userform.is_valid() and addressform.is_valid():

            userform.save()
            addressform.save()

            return HttpResponseRedirect(reverse('home:profile'))
    return render(request,'home/update_details.html',{'userform':userform,'addressform':addressform})

@login_required
def Update_Password(request):
    if request.method == "POST":
        password = request.POST.get('password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        user = authenticate(username=request.user.username,password=password)
        form=request.user

        if user:
            print(user)
            if new_password == confirm_password:
                print(new_password==confirm_password)
                curuser=request.user
                #curuser.password=new_password
                curuser.set_password(new_password)
                curuser.save()
                update_session_auth_hash(request, form)
                return HttpResponseRedirect(reverse('home:profile'))
    return render(request,'home/password.html',)


# class UserAddressList(APIView):
#
#     def get(self, request):
#         people = UserAddress.objects.all()
#         serializer = UserAddressSerializer(people, many=True)
#         return Response(serializer.data)
