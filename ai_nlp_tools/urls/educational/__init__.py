from django.urls import path, include

urlpatterns = [
    path("research-paper/", include("ai_nlp_tools.urls.educational.research_paper"), name="research-paper-writer"),
    path("", include("ai_nlp_tools.urls.educational.")),
    path("", include("ai_nlp_tools.urls.educational.")),
    path("", include("ai_nlp_tools.urls.educational.")),

]
