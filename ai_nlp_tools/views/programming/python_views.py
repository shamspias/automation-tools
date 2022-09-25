from rest_framework.views import APIView, Response
from rest_framework import status
from ai_nlp_tools.serializers import ProgrammingSerializers
from ai_nlp_tools.utils import (
    one_line_list_comprehension,
    one_line_dist_comprehension,
    one_line_generator,
)


class OneLineListComprehensionAPIView(APIView):
    """
    API View to generate one line list
    """
    serializer_class = ProgrammingSerializers

    def post(self, request, *args, **kwargs):
        """
        Give python code
        {
            "code": "Your code"
        }
        """
        title = request.data.get('title')
        try:
            return Response(one_line_list_comprehension(title), status=status.HTTP_200_OK)
        except:
            return Response({"error": "Not Found"}, status=status.HTTP_204_NO_CONTENT)
