from rest_framework import serializers as Serializers
#from rest_framework import employees
from . models import *
class employeesSerializer(Serializers.ModelSerializer):
    class Meta:
        model = employees
#    fields = ('firstname', 'lastname')
        fields = '__all__'