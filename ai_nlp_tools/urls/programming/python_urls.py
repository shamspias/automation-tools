from django.urls import path
from ai_nlp_tools.views import OneLineListComprehensionAPIView

urlpatterns = [
    path("list-comprehension", OneLineListComprehensionAPIView.as_view(), name="ai-python-code"),

]
