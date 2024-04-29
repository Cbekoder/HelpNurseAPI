from rest_framework import serializers
from .models import Service, Nurse, Hospital, NurseService, HospitalService

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class NurseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nurse
        fields = '__all__'

class HospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hospital
        fields = '__all__'

class NurseServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = NurseService
        fields = '__all__'

class HospitalServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = HospitalService
        fields = '__all__'
