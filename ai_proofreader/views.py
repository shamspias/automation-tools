from rest_framework.views import APIView, Response
from .utils import ai_proofreading


class ProofreaderAPIView(APIView):
    """
    API View to get word and send 
    """

    def post(self, request, *args, **kwargs):
        word = request.POST.get('word', '')
        return Response(ai_proofreading(word))
