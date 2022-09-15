from rest_framework import status
from rest_framework.views import APIView, Response

from .serializers import ProofreadingSerializers, ProofreadingFileSerializers
from .utils import ai_proofreading


class ProofreaderAPIView(APIView):
    """
    API View to get word
    Example:
    {
        "word": "Hello There"
    }

    """
    serializer_class = ProofreadingSerializers

    def post(self, request, *args, **kwargs):
        """
        Get correct word
        :param request: string
        :param args: word
        :param kwargs:
        :return:
        """
        word = request.data.get('word', '')
        return Response(ai_proofreading(word), status=status.HTTP_200_OK)


class ProofreaderDocumentAPIView(APIView):
    """
    API View to get word
    Example:
    {
        "word": "Hello There"
    }

    """
    serializer_class = ProofreadingFileSerializers

    def post(self, request, *args, **kwargs):
        """
        Get correct word
        :param request: string
        :param args: word
        :param kwargs:
        :return:
        """
        word = request.FILES.get('document')
        return Response(ai_proofreading(word), status=status.HTTP_200_OK)
