from django.http import HttpResponse
from .forms import requestorForm,landmarkForm
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, QueryDict
from home.models import *

def load_cities(request):
    # print("sdhksdsknsl")
    try:
        state_id = request.POST.get('state')
        cities = City.objects.filter(state_id=state_id).order_by('name')

    except:
        cities = City.objects.none()


    #print(state_id)

    # print(cities)
    return render(request, 'requestor/dropdown.html', {'cities': cities})

# Create your views here.

def index(request):
    form = requestorForm()
    landmarkform=landmarkForm()
    if request.user.is_authenticated:
        try:
            if request.user.new_requestor:
                return HttpResponseRedirect(reverse("requestor:profile"))

        except:
            return HttpResponseRedirect(reverse("home:profile"))
    if request.method=="POST":
        form = requestorForm(data = request.POST);
        landmarkform=landmarkForm(data = request.POST)

        if form.is_valid() and landmarkform.is_valid():
            user=form.save(commit=False)
            landmark=landmarkform.save()
            user.set_password(user.password)
            user.save()
            user.is_active = False

            return HttpResponse("Your registration has been taken")
        else:
            messages.error(request, 'This Email or Username already exist')

    return render(request,'requestor/signup.html',{'form':form,'landmarkform':landmarkform})


@login_required
def requestor_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home:index'))


def requestor_Login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("requestor:profile"))

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


    return render(request,'requestor/login.html',)



@login_required
def profile(request):
    return render(request,'requestor/profile.html',)
