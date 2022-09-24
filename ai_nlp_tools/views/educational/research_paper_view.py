from rest_framework.views import APIView, Response
from rest_framework import status
from ai_nlp_tools.serializers import ResearchPaperSerializers
from ai_nlp_tools.utils import normal_research_paper


class NormalResearchPaperAPIView(APIView):
    """
    API View for normal Research Paper
    """
    serializer_class = ResearchPaperSerializers

    def post(self, request, *args, **kwargs):
        """
        Give Research Paper Title
        {
            "title": "Your text"
        }
        """
        title = request.data.get('title', '')
        return Response(normal_research_paper(title), status=status.HTTP_200_OK)
