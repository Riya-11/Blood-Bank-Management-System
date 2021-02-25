import datetime
from django.shortcuts import render
from home.models import UserHistory

def index (request):
    content = {'historys' : UserHistory.objects.order_by('-donation_date') , 'datenow' : datetime.datetime.now()}

    return render(request,'display/index.html',content)
