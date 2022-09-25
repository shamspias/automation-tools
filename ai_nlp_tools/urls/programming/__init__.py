from django.urls import path, include

urlpatterns = [
    path("python/", include("ai_nlp_tools.urls.programming.python_urls"), name="ai-python-code"),

]
