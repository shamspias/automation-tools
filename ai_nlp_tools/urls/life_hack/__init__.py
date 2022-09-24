from django.urls import path, include

urlpatterns = [
    path("song", include("ai_nlp_tools.urls.life_hack.song")),
    path("", include("ai_nlp_tools.urls.life_hack.")),
    path("", include("ai_nlp_tools.urls.life_hack.")),
    path("", include("ai_nlp_tools.urls.life_hack.")),

]
