import datetime

from drf_writable_nested import WritableNestedModelSerializer
from rest_framework.exceptions import ValidationError

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
    next_exercise_date = serializers.SerializerMethodField()

    class Meta:
        model = Exercise
        fields = ['id', 'title', 'execute_date', 'specialization', 'periodicity',
                  'patient', 'doctor', 'next_exercise_date']

    def get_next_exercise_date(self, instance):
        result = instance.execute_date + datetime.timedelta(days=instance.periodicity)
        return result

    def validate(self, attrs):
        specialization_data = attrs.get('specialization')

        if self.instance:
            specialization = self.instance.specialization
        else:
            specialization = None

        if specialization is not None:
            if specialization_data != "PHY":
                raise ValidationError("Exercises can only be changed by a physiotherapist")

        super().validate(attrs)

        return attrs
