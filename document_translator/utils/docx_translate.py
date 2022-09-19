from .translate_core import language_translation
from django.conf import settings


class TranslateDocx:
    def translate_docx(self, doc_file, source_ln="auto", target_ln="en", proofread=False):
        """
        translate the word
        """
        doc_file_name = doc_file.name
        word_file = target_ln + "_" + doc_file_name
        if proofread:
            new_docx_file_name = settings.CONVERTED_FILE_LOCATION + "proofread/" + word_file
            language_translation(doc_file.my_file.path, new_docx_file_name, source_ln, target_ln, proofread=proofread)
            return "proofread/" + word_file
        else:
            new_docx_file_name = settings.CONVERTED_FILE_LOCATION + "translated/" + word_file
            language_translation(doc_file.my_file.path, new_docx_file_name, source_ln, target_ln, proofread=proofread)
            return "translated/" + word_file
