from django.urls import path
from .views import TextToXMLAPIView

urlpatterns = [
    path("convert/", TextToXMLAPIView.as_view(), name="convert-to-xml"),
]
