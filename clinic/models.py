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


daily = 'DAY'
one_day = 'ONE'
two_days = 'TWO'
three_days = 'THR'

OPTIONS_PERIODICITY = [
    (daily, 'daily'),
    (one_day, 'one_day'),
    (two_days, 'two_days'),
    (three_days, 'three_days')
]


class Exercise(models.Model):
    class Direction(models.TextChoices):
        PHYSIOTHERAPIST = 'PHY', 'Physiotherapist'
        PSYCHOLOGIST = 'PSY', 'Psychologist'
    title = models.CharField(max_length=255)
    start_date = models.DateField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, blank=True)
    specialization = models.CharField(max_length=3, choices=Direction.choices)
    periodicity = models.CharField(max_length=3, choices=OPTIONS_PERIODICITY)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
