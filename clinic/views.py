
from rest_framework import viewsets
from django_filters import rest_framework as df_filters

from .serializers import ExerciseSerializer
from .models import *


class ExerciseFilter(df_filters.FilterSet):
    class Meta:
        model = Exercise
        fields = ['doctor__last_name', 'patient__last_name']


class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    http_method_names = ['get', 'post', 'patch', 'delete', 'put', 'options']
    filter_backends = [df_filters.DjangoFilterBackend]
    filterset_class = ExerciseFilter


