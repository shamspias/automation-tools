from django.urls import path
from ai_nlp_tools.views import NormalResearchPaperAPIView

urlpatterns = [
    path("", NormalResearchPaperAPIView.as_view(), name="normal-research-paper-writer"),
    path("medical", NormalResearchPaperAPIView.as_view(), name="medical-research-paper-writer"),
    path("marketing", NormalResearchPaperAPIView.as_view(), name="marketing-research-paper-writer"),
    path("tech", NormalResearchPaperAPIView.as_view(), name="tech-research-paper-writer"),
    path("survey", NormalResearchPaperAPIView.as_view(), name="survey-research-paper-writer"),
    path("case-study", NormalResearchPaperAPIView.as_view(), name="case-study-research-paper-writer"),
]
