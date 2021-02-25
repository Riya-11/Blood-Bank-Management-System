from .models import *
from django import forms


class VolunteerForm(forms.ModelForm):
    class Meta:
        model = BloodVolunteer
        fields = '__all__'


class newcamp(forms.ModelForm):
    class Meta:
        model = BloodCamp
        fields = ('campid', 'startdate', 'enddate', 'location')


class newdonor(forms.ModelForm):
    class Meta:
        model = BloodCampDonor
        fields = ('firstname','lastname','email','phone','gender','blood','bloodcamp')
    def __init__(self, status, *args, **kwargs):
        super(newdonor, self).__init__(*args, **kwargs)
        self.fields['bloodcamp'].queryset = BloodCamp.objects.filter(status=status)
