from django.urls import path, include

urlpatterns = [
    path("education/", include("ai_nlp_tools.urls.educational")),
    # path("life-hack/", include("ai_nlp_tools.urls.life_hack")),
    # path("programming/", include("ai_nlp_tools.urls.programming")),
    # path("marketing/", include("ai_nlp_tools.urls.marketing")),
]
