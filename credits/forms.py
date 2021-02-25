from django import forms
from .models import Transaction
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.http import HttpResponse

class Org(forms.ModelForm):
    class Meta:
        model = Transaction
        exclude = ['transactionid','wallet','date','initialcredit','aftercredit','getcredit']
        
