from django.contrib import admin

# Register your models here.
from .models import *
#from django.contrib.auth.models import User

admin.site.register(UserAddress)
admin.site.register(UserProfile)
admin.site.register(UserHistory)
admin.site.register(City)
admin.site.register(State)
