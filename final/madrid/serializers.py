from rest_framework import serializers
from .models import Footballer
class FootballSerializer(serializers.ModelSerializer):
    class Meta:
        model = Footballer
        fields = ['id' , 'name' , 'position' , 'bio']

