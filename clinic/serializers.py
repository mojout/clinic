from drf_writable_nested import WritableNestedModelSerializer

from .models import *
from rest_framework import serializers


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'email', 'phone']


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = ['first_name', 'last_name', 'position']


class ExerciseSerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    patient = PatientSerializer()
    doctor = DoctorSerializer()

    class Meta:
        model = Exercise
        fields = ['id', 'title', 'start_date', 'updated', 'specialization', 'periodicity',
                  'patient', 'doctor']
