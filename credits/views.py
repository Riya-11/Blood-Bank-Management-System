from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Wallet,Transaction
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from . import forms
from django.core.mail import send_mail
from django.views.decorators.cache import cache_control
from django.urls import reverse


@login_required
def insert(request):
	if request.method == 'POST':
		user = request.user
		creditsnow = request.POST['credits']
		organisation = request.POST['organisation']
		email = user.email
		wt = Wallet.objects.get(user = user)
		ic = wt.credit
		gc = -1 * int(creditsnow)
		if int(creditsnow) <= wt.credit:
			wt.credit -= int(creditsnow)
			ac = wt.credit
			wt.save()
			p = Transaction(wallet = wt , initialcredit =ic , aftercredit = ac , getcredit= gc, organisation=organisation)
			p.save()
			try:
				send_mail(
				'Blood Bank',
				'Name          :' + str(user) + '\n' +
				'Id            :' + str(p.transactionid) + '\n' +
				'Organisation  :' + str(organisation) + '\n' +
				'Credits 	   :' + str(creditsnow) + '\n',
				'29riyajain@gmail.com',
				[email],
				fail_silently = False,
				)
				return render(request,'credits/success.html')
			except:
				wt.credit += int(creditsnow)
				wt.save()
				gc = -1 * gc
				p = Transaction(wallet = wt , initialcredit =ac , aftercredit = ic , getcredit= gc, organisation= "Transaction Failed")
				p.save()
				return render(request,'credits/fail1.html')
		else:
			return render(request,'credits/fail.html')
	return render(request,'credits/fail.html')

@login_required
def index(request):
	user = request.user
	userform=forms.Org()
	try:
		coins = Wallet.objects.get(user = user)
	except:
		return HttpResponseRedirect(reverse('home:index'))
	content = { 'coins' : coins , 'org':userform}
	return render(request,'credits/index.html',content)

@login_required
def history(request):
	user = request.user
	nulllist = []
	co = Transaction.objects.all()
	for i in range(0,len(co)):
		if co[i].wallet.user == user:
			nulllist.append(co[i])
	content = {'coins' : nulllist}
	return render(request,'credits/history.html',content)
