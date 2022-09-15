from django.urls import path
from .views import (
    TranslateDocumentAPIView,
    TranslatePDFAPIView,
    TranslateAudioAPIView,
    TranslateVideoAPIView
)

urlpatterns = [
    path('pdf/', TranslatePDFAPIView.as_view(), name='translate-pdf'),
    path('docx/', TranslateDocumentAPIView.as_view(), name='translate-docx'),
    path('audio/', TranslateVideoAPIView.as_view(), name='translate-audio'),
    path('video/', TranslateVideoAPIView.as_view(), name='translate-video'),
]
