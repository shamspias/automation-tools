from django.urls import path
from .views import BlogWriterAPIView

urlpatterns = [
    path("", BlogWriterAPIView.as_view(), name="blog-writer")
]
