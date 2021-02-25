from django.shortcuts import render
from django.http import HttpResponse
from .models import BloodBankName,PathlabName

def index(request):
	Bn = BloodBankName.objects.all()
	Bloodbank = []
	latitude = []
	longitude = []		
	for i in range(0,len(Bn)):
		Bloodbank.append(Bn[i].bloodbankname)
		latitude.append(Bn[i].latitude)
		longitude.append(Bn[i].longitude)	
	return render(request, 'maps/map.html',{'names':Bloodbank,'lat':latitude,'lng':longitude})
	
def index1(request):
	Bn = PathlabName.objects.all()
	Pathlab = []
	latitude = []
	longitude = []		
	for i in range(0,len(Bn)):
		Pathlab.append(Bn[i].pathlabname)
		latitude.append(Bn[i].latitude)
		longitude.append(Bn[i].longitude)	
	return render(request, 'maps/map1.html',{'names':Pathlab,'lat':latitude,'lng':longitude})
