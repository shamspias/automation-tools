from rest_framework.views import APIView, Response
from rest_framework import status
from .serializers import BlogSerializers
from .utils import (
    generate_blog_topics,
    generate_blog_sections,
    blog_section_expander
)


class TopicAPIView(APIView):
    """
    API View to get blog topic names
    """
    serializer_class = BlogSerializers

    def post(self, request, *args, **kwargs):
        """
        Blog topic names
        {
            "topic": "Your text"
        }
        """
        topic = request.data.get('topic', '')
        return Response(generate_blog_topics(topic), status=status.HTTP_200_OK)


class SectionsAPIView(APIView):
    """
    API View to get blog section names from topic
    """
    serializer_class = BlogSerializers

    def post(self, request, *args, **kwargs):
        """
        Blog section names from topic
        {
            "topic": "Your text"
        }
        """
        topic = request.data.get('topic', '')
        return Response(generate_blog_sections(topic), status=status.HTTP_200_OK)


class SectionDetailsAPIView(APIView):
    """
    API View to get blog section details from section with topic
    """
    serializer_class = BlogSerializers

    def post(self, request, *args, **kwargs):
        """
        Blog section details get from section with topic
        {
            "topic": "Your text" ,
            "section": "Introduction"
        }
        """
        topic = request.data.get('topic', '')
        section = request.data.get('section', '')
        return Response(blog_section_expander(topic, section), status=status.HTTP_200_OK)
