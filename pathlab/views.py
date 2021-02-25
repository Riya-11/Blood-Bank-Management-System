from django.shortcuts import render
from .models import PathLabUser2
from .forms import PathlabForm2
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.contrib.auth.models import User
from home.models import UserProfile
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PathLabUser2serializer
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import status



@login_required(login_url='/home/login')
def index(request):
    return render(request, 'pathlab/index.html')


@login_required(login_url='/home/login')
def booko(request):
    if request.method == 'POST':
        form = PathlabForm2(request.POST)
        #form = NameForm(request.POST)
        if form.is_valid():
            result = PathLabUser2.objects.all()
            context = {'result': result, 'form': form, }
            return render(request, 'pathlab/booko.html', context)

    else:
        form = PathlabForm2()
    return render(request, 'pathlab/booko.html', {'form': form})


@login_required(login_url='/home/login')
def result(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        address = request.POST['address']
        bloodgroup = request.POST['bloodgroup']
        testtype = request.POST['testtype']
        user = request.user
        if user.is_authenticated:
            p = UserProfile.objects.get(user = user)

            PathLabUser2.objects.create(firstname=firstname, lastname=lastname, address=address, bloodgroup=bloodgroup, testtype=testtype, profile=p)
        print("oihnohnon")
        email = user.email

        send_mail(
            'Blood Test Booked',
            'Your request for Blood Test is received and it is being processed. \n'
            'Details: \n'
            'Name          :' + str(firstname) + str(lastname) + '\n' +
            'Blood Group   :' + str(bloodgroup) + '\n' +
            'Test Type     :' + str(testtype) + '\n',
            'kartikkapoor13@gmail.com',
            [email],
            fail_silently = False,
            )

    return render(request, 'pathlab/result.html')

@login_required(login_url='/home/login')
def history(request):
    datalist = {}
    user = request.user
    if user.is_authenticated:
        p = UserProfile.objects.get(user = user)
        result = PathLabUser2.objects.filter(profile=p)
    #print(result)        #print(datalist)
    #print(datalist)

    context = {'result': result}
    return render(request, 'pathlab/history.html', context)


@login_required(login_url='/home/login')
def report(request, rid):
    reports = PathLabUser2.objects.get(id=rid)
    context = {'reports': reports}
    return render(request, 'pathlab/report.html', context)

#@login_required(login_url='/home/login')
class PathLabUser2class(APIView):
    def get(self, request):
        datalog = PathLabUser2.objects.all()
        serializer = PathLabUser2serializer(datalog, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PathLabUser2serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)


'''class PathLabUser2class(viewsets.ModelViewSet):
    queryset = PathLabUser2.objects.all()
    serializer_class = PathLabUser2serializer'''