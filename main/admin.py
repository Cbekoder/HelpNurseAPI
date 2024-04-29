from django.contrib import admin
from .models import Service, Nurse, Hospital, NurseService, HospitalService

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Nurse)
class NurseAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'gender', 'phone_number', 'long', 'lat')

@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'working_hours', 'working_days', 'long', 'lat')

@admin.register(NurseService)
class NurseServiceAdmin(admin.ModelAdmin):
    list_display = ('nurse', 'service')

@admin.register(HospitalService)
class HospitalServiceAdmin(admin.ModelAdmin):
    list_display = ('hospital', 'service')
