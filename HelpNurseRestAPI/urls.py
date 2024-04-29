from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from main.views import (ServiceViewSet, NurseViewSet,
                        HospitalViewSet, NurseServiceAPIView,
                        HospitalServiceViewSet, LocationalNurseApiView,
                        LocationalHospitalApiView, HospitalServiceAPIView)

router = DefaultRouter()
router.register(r'services', ServiceViewSet)
router.register(r'nurses', NurseViewSet)
router.register(r'hospitals', HospitalViewSet)
router.register(r'hospital-services', HospitalServiceViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('locationalNurse/<str:long>/<str:lat>/<str:service>', LocationalNurseApiView.as_view()),
    path('locationalHospital/<str:long>/<str:lat>/<str:service>', LocationalHospitalApiView.as_view()),
    path('nurse_service/<int:service>/<int:nurse>/', NurseServiceAPIView.as_view()),
    path('hospital_service/<int:service>/<int:hospital>/', HospitalServiceAPIView.as_view()),
]
