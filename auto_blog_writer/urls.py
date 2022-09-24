from django.urls import path
from .views import (
    TopicAPIView,
    SectionsAPIView,
    SectionDetailsAPIView
)

urlpatterns = [
    path("", TopicAPIView.as_view(), name="blog-writer-topic"),
    path("/sections", SectionsAPIView.as_view(), name="blog-writer-sections"),
    path("/sections/details", SectionDetailsAPIView.as_view(), name="blog-writer-extend-sections"),
]
