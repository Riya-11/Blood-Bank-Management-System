from rest_framework import serializers
from .models import PathLabUser2

class PathLabUser2serializer(serializers.ModelSerializer):

    class Meta:
        model = PathLabUser2
        fields = ('firstname', 'lastname', 'profile', 'address', 'bloodgroup', 'testtype', 'date', 'Result', 'feedback')