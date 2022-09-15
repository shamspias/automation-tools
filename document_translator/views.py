from rest_framework import status
from rest_framework.views import APIView, Response

from .serializers import TranslationFileSerializers

from .utils import (
    TranslateDocx,
    TranslatePDF,
    AudioVideoTranslate,
)


class TranslateDocumentAPIView(APIView):
    """
    API View for Docx file translation
    """
    serializer_class = TranslationFileSerializers
    td = TranslateDocx()

    def post(self, request, *args, **kwargs):
        source_ln = request.data.get('source_ln', '')
        target_ln = request.data.get('target_ln', '')
        document = request.FILES.get('document', '')
        return Response(
            self.td.translate_docx(doc_file=document, source_ln=source_ln, target_ln=target_ln),
            status=status.HTTP_200_OK)


class TranslatePDFAPIView(APIView):
    """
    API View for PDF file translation
    """
    serializer_class = TranslationFileSerializers
    tp = TranslatePDF()

    def post(self, request, *args, **kwargs):
        source_ln = request.data.get('source_ln', '')
        target_ln = request.data.get('target_ln', '')
        document = request.FILES.get('document', '')
        return Response(
            self.tp.translate_pdf(pdf_file=document, source_ln=source_ln, target_ln=target_ln),
            status=status.HTTP_200_OK)


class TranslateVideoAPIView(APIView):
    """
    API View for Video file translation
    """
    serializer_class = TranslationFileSerializers
    avt = AudioVideoTranslate()

    def post(self, request, *args, **kwargs):
        """
        Get correct word
        :param request: string
        :param args: word
        :param kwargs:
        :return:
        """
        document = request.FILES.get('document')
        return Response(self.avt.translate_video(document), status=status.HTTP_200_OK)


class TranslateAudioAPIView(APIView):
    """
    API View for Audio file translation
    """
    serializer_class = TranslationFileSerializers
    avt = AudioVideoTranslate()

    def post(self, request, *args, **kwargs):
        """
        Get correct word
        :param request: string
        :param args: word
        :param kwargs:
        :return:
        """
        document = request.FILES.get('document')
        return Response(self.avt.translate_audio(document), status=status.HTTP_200_OK)
