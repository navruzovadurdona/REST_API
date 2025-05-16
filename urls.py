from django.urls import path
from .views import convert_to_xml

urlpatterns = [
    path('convert/', convert_to_xml, name='convert_to_xml'),
]
