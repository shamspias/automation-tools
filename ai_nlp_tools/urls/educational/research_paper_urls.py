from django.urls import path
from ai_nlp_tools.views import ResearchPaperSectionAPIView, ResearchPaperSectionExpanderAPIView

urlpatterns = [
    path("sections", ResearchPaperSectionAPIView.as_view(), name="research-paper-writer-sections"),
    path("sections/expand", ResearchPaperSectionExpanderAPIView.as_view(), name="research-paper-writer-section-expand"),
]
