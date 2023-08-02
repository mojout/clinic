from rest_framework import routers
from clinic.views import ExerciseViewSet
from django.urls import path, include
from .yasg import urlpatterns as doc_urls

router = routers.DefaultRouter()
router.register(r'patientcard', ExerciseViewSet, basename='patientcard')

urlpatterns = [
    path('', include(router.urls)),
    # path('patientcard/<int:pk>/', ExerciseViewSetDetail.as_view, name='get_data'),

]

urlpatterns += doc_urls
