import random
import string
from rest_framework import status
from rest_framework.views import APIView, Response
from .models import TranslatedFile

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
        if document:
            random_name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
            new_name = random_name + document.name

            _file = TranslatedFile.objects.create(name=new_name, my_file=document)
            file_obj = TranslatedFile.objects.get(name__exact=new_name)

            translated_file = self.td.translate_docx(doc_file=file_obj, source_ln=source_ln, target_ln=target_ln)
            file_obj.translated_file = translated_file[0]
            file_obj.save()
            context = {
                "number_of_words": translated_file[1],
                "url": file_obj.translated_file.url
            }

            return Response(context, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


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
        if document:
            random_name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
            new_name = random_name + document.name

            _file = TranslatedFile.objects.create(name=new_name, my_file=document)
            file_obj = TranslatedFile.objects.get(name__exact=new_name)

            translated_file = self.tp.translate_pdf(pdf_file=file_obj, source_ln=source_ln, target_ln=target_ln)
            file_obj.translated_file = translated_file[0]
            file_obj.save()
            context = {
                "number_of_words": translated_file[1],
                "url": file_obj.translated_file.url
            }

            return Response(context, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


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
        source_ln = request.data.get('source_ln', '')
        target_ln = request.data.get('target_ln', '')
        duration = request.data.get('duration', '')
        document = request.FILES.get('document')
        return Response(self.avt.translate_video(video_file=document, source_lan=source_ln, target_lan=target_ln,
                                                 duration=duration), status=status.HTTP_200_OK)


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
        source_ln = request.data.get('source_ln', 'auto')
        target_ln = request.data.get('target_ln', 'de')
        duration = request.data.get('duration', '')
        document = request.FILES.get('document')
        if document:
            return Response(self.avt.translate_audio(audio_file=document, source_lan=source_ln, target_lan=target_ln,
                                                     duration=duration), status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)
