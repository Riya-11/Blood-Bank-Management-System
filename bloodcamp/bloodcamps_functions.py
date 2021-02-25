from datetime import date
from .models import BloodCamp
def checkdate(o):
    if (date.today() > o.enddate):
        print('check 1')
        return '1'
    elif (date.today() < o.startdate):
        print('check 3')
        return '3'
    else:
        print('check 2')
        return '2'


def default_fun(request):
    camps = BloodCamp.objects.all()
    for camp in camps:
        if checkdate(camp) == '1':
            print('is 1')
            camp.status = '1'
            camp.save()
        elif checkdate(camp) == '2':
            print('is 2')
            camp.status = '2'
            camp.save()
        elif checkdate(camp) == '3':
            print('is 3')
            camp.status = '3'
            camp.save()
