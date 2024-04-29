from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Nurse(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    photo = models.JSONField(blank=True, null=True)
    phone_number = models.CharField(max_length=15)
    long = models.FloatField()
    lat = models.FloatField()

    def __str__(self):
        return self.name

class Hospital(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    working_hours = models.CharField(max_length=100)
    working_days = models.CharField(max_length=100)
    long = models.FloatField()
    lat = models.FloatField()

    def __str__(self):
        return self.name

class NurseService(models.Model):
    nurse = models.ForeignKey(Nurse, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    def __str__(self):
        return self.nurse.name

class HospitalService(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    def __str__(self):
        return self.hospital.name