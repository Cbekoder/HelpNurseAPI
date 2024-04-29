from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Service, Nurse, Hospital, NurseService, HospitalService
from .serializers import ServiceSerializer, NurseSerializer, HospitalSerializer, NurseServiceSerializer, HospitalServiceSerializer
from math import radians, sin, cos, sqrt, atan2

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class NurseViewSet(viewsets.ModelViewSet):
    queryset = Nurse.objects.all()
    serializer_class = NurseSerializer

class HospitalViewSet(viewsets.ModelViewSet):
    queryset = Hospital.objects.all()
    serializer_class = HospitalSerializer

class NurseServiceAPIView(APIView):
    def get(self, request, service, nurse):
        nurse = Nurse.objects.get(id=nurse)
        service = Service.objects.get(id=service)
        NurseService.objects.create(nurse=nurse, service=service)
        nurse_services = NurseService.objects.filter(nurse=nurse).values_list('service', flat=True)
        services = Service.objects.exclude(id__in=nurse_services)
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data)

class HospitalServiceAPIView(APIView):
    def get(self, request, service, hospital):
        nurse = Hospital.objects.get(id=hospital)
        service = Service.objects.get(id=service)
        HospitalService.objects.create(hospital=hospital, service=service)
        hospital_services = HospitalService.objects.filter(hospital=hospital).values_list('service', flat=True)
        services = Service.objects.exclude(id__in=hospital_services)
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data)

class HospitalServiceViewSet(viewsets.ModelViewSet):
    queryset = HospitalService.objects.all()
    serializer_class = HospitalServiceSerializer

class LocationalNurseApiView(APIView):
    def get(self, request, long, lat, service):
        long = float(long)
        lat = float(lat)

        nurses = Nurse.objects.all()
        service = NurseService.objects.filter(id=service).values_list('nurse', flat=True)
        nearby_nurses = []
        for nurse in nurses:
            if nurse.id in service:
                distance = calculate_distance(lat, long, nurse.lat, nurse.long)
                if distance <= 10:
                    nearby_nurses.append({
                        'id': nurse.id,
                        'name': nurse.name,
                        'age': nurse.age,
                        'gender': nurse.gender,
                        'photo': nurse.photo,
                        'phone_number': nurse.phone_number,
                        'long': nurse.long,
                        'lat': nurse.lat,
                        'distance': distance
                    })
        nearby_nurses.sort(key=lambda x: x['distance'])

        return Response(nearby_nurses)

class LocationalHospitalApiView(APIView):
    def get(self, request, long, lat, service):
        long = float(long)
        lat = float(lat)

        hospitals = Hospital.objects.all()
        service = NurseService.objects.filter(id=service).values_list('nurse', flat=True)
        nearby_hospitals = []
        for hospital in hospitals:
            if hospital.id in service:
                distance = calculate_distance(lat, long, hospital.lat, hospital.long)
                if distance <= 50:
                    nearby_hospitals.append({
                        'id': hospital.id,
                        'name': hospital.name,
                        'working_hours': hospital.working_hours,
                        'working_days': hospital.working_days,
                        'phone_number': hospital.phone_number,
                        'long': hospital.long,
                        'lat': hospital.lat,
                        'distance': distance
                    })
        nearby_hospitals.sort(key=lambda x: x['distance'])

        return Response(nearby_hospitals)


def calculate_distance(lat1, lon1, lat2, lon2):
    R = 6371.0
    lat1_rad = radians(lat1)
    lon1_rad = radians(lon1)
    lat2_rad = radians(lat2)
    lon2_rad = radians(lon2)
    dlon = lon2_rad - lon1_rad
    dlat = lat2_rad - lat1_rad
    a = sin(dlat / 2)**2 + cos(lat1_rad) * cos(lat2_rad) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    return distance
