from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Patient(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, blank=True)
    phone = models.CharField(max_length=12, blank=True)


class Doctor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)


class Exercise(models.Model):
    class Direction(models.TextChoices):
        PHYSIOTHERAPIST = 'PHY', 'Physiotherapist'
        PSYCHOLOGIST = 'PSY', 'Psychologist'

    title = models.CharField(max_length=255)
    execute_date = models.DateField(auto_now_add=True)
    specialization = models.CharField(max_length=3, choices=Direction.choices)
    periodicity = models.IntegerField(
                                      validators=[
                                          MaxValueValidator(100),
                                          MinValueValidator(1)
                                      ])
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
