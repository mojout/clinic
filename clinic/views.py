from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets, status
from django_filters import rest_framework as df_filters
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from .serializers import ExerciseSerializer
from .models import *


class ExerciseFilter(df_filters.FilterSet):
    class Meta:
        model = Exercise
        fields = ['doctor__last_name', 'patient__last_name', 'periodicity']


class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all().prefetch_related('patient', 'doctor')
    serializer_class = ExerciseSerializer
    http_method_names = ['get', 'post', 'patch', 'delete', 'put', 'options']
    filter_backends = [df_filters.DjangoFilterBackend]
    filterset_class = ExerciseFilter


