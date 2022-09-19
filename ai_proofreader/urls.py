from django.urls import path
from .views import ProofreaderAPIView, ProofreaderDocumentAPIView

urlpatterns = [
    path("", ProofreaderAPIView.as_view(), name="proofreader"),
    path("document/", ProofreaderDocumentAPIView.as_view(), name="proofreader-document")
]
