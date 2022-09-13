from django.urls import path
from .views import ProofreaderAPIView

urlpatterns = [
    path("", ProofreaderAPIView.as_view(), name="proofreader")
]
