from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('clinic.urls')),
    path('swagger-ui/', TemplateView.as_view(
        template_name='../templates/swagger-ui.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),
    path('openapi/', get_schema_view(
        title="Patient card",
        description="UrbanMedic",
        version="0.1",
    ), name='openapi-schema'),
]
