from rest_framework.views import APIView, Response
from rest_framework import status
from ai_nlp_tools.serializers import ResearchPaperSerializers
from ai_nlp_tools.utils import research_paper_sections, research_paper_section_expander, generate_research_paper_topics


class ResearchPaperTopicAPIView(APIView):
    """
    API View to generate Topic for Research Paper
    """
    serializer_class = ResearchPaperSerializers

    def post(self, request, *args, **kwargs):
        """
        Give Research Paper Title
        {
            "title": "Your text"
        }
        """
        title = request.data.get('title')
        try:
            return Response(generate_research_paper_topics(title), status=status.HTTP_200_OK)
        except:
            return Response({"error": "Not Found"}, status=status.HTTP_204_NO_CONTENT)


class ResearchPaperSectionAPIView(APIView):
    """
    API View to generate sections for Research Paper
    """
    serializer_class = ResearchPaperSerializers

    def post(self, request, *args, **kwargs):
        """
        Give Research Paper Title
        {
            "title": "Your text"
        }
        """
        title = request.data.get('title')
        try:
            return Response(research_paper_sections(title), status=status.HTTP_200_OK)
        except:
            return Response({"error": "Not Found"}, status=status.HTTP_204_NO_CONTENT)


class ResearchPaperSectionExpanderAPIView(APIView):
    """
    API View to expand sections for Research Paper
    """
    serializer_class = ResearchPaperSerializers

    def post(self, request, *args, **kwargs):
        """
        Give Research Paper Title
        {
            "section": "Your text",
            "title": "Your text"
        }
        """
        section = request.data.get('section')
        title = request.data.get('title')
        try:
            return Response(research_paper_section_expander(section, title), status=status.HTTP_200_OK)
        except:
            return Response({"error": "Not Found"}, status=status.HTTP_204_NO_CONTENT)
