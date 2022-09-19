import random
import string
from rest_framework import status
from rest_framework.views import APIView, Response

from .serializers import ProofreadingSerializers, ProofreadingFileSerializers
from .models import Proofreading
from .utils import ai_proofreading
from document_translator.utils import (
    TranslateDocx,
    TranslatePDF,
    AudioVideoTranslate,
)


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
    tp = TranslatePDF()
    td = TranslateDocx()

    def post(self, request, *args, **kwargs):
        """
        Get correct word
        :param request: string
        :param args: word
        :param kwargs:
        :return:
        """
        document = request.FILES.get('document', '')
        if document:
            random_name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
            new_name = random_name + document.name

            _file = Proofreading.objects.create(name=new_name, my_file=document)
            file_obj = Proofreading.objects.get(name__exact=new_name)

            if file_obj.check_pdf:
                translated_file = self.tp.translate_pdf(pdf_file=file_obj, proofread=True)
            elif file_obj.check_docx:
                translated_file = self.td.translate_docx(doc_file=file_obj, proofread=True)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)

            file_obj.proofread_file = translated_file
            file_obj.save()

            return Response(file_obj.proofread_file.url, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
