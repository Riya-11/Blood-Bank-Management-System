from django import forms
from .models import PathLabUser2
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.http import HttpResponse


'''class PathlabForm(forms.ModelForm):
    class Meta:
        model = PathLabUser
        fields = ['testtype']
'''

class PathlabForm2(forms.ModelForm):
    class Meta:
        model = PathLabUser2
        fields = ['firstname', 'lastname', 'address', 'bloodgroup', 'testtype']

