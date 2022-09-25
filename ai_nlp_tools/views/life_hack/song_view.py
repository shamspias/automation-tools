from rest_framework.views import APIView, Response
from rest_framework import status
from ai_nlp_tools.serializers import SongSerializers
from ai_nlp_tools.utils import normal_song, categories_song


class NormalSongAPIView(APIView):
    """
    API View to generate Songs
    """
    serializer_class = SongSerializers

    def post(self, request, *args, **kwargs):
        """
        Give Songs topic
        {
            "topic": "Hey there",
        }
        """
        title = request.data.get('topic')

        try:
            return Response(normal_song(title), status=status.HTTP_200_OK)
        except:
            return Response({"error": "Not Found"}, status=status.HTTP_204_NO_CONTENT)


class CategoriesSongAPIView(APIView):
    """
    API View to generate Songs with specific categories
    """
    serializer_class = SongSerializers

    def post(self, request, *args, **kwargs):
        """
        Give Songs topic
        {
            "topic": "Hey there",
            "categories": "Love song"
        }
        """
        title = request.data.get('topic')
        categories = request.data.get('categories')
        try:
            return Response(categories_song(categories, title), status=status.HTTP_200_OK)

        except:
            return Response({"error": "Not Found"}, status=status.HTTP_204_NO_CONTENT)
