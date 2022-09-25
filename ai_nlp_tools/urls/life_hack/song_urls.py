from django.urls import path
from ai_nlp_tools.views import NormalSongAPIView, CategoriesSongAPIView

urlpatterns = [
    path("", NormalSongAPIView.as_view(), name="ai-song-writer"),
    path("category", CategoriesSongAPIView.as_view(), name="ai-song-writer-category"),
]
