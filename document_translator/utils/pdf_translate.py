from pdf2docx import parse
import os
from .translate_core import language_translation
import subprocess
from django.conf import settings


class TranslatePDF:

    def doc2pdf_linux(self, doc, proofread=False):
        """
        convert a doc/docx document to pdf format (linux only, requires libreoffice)
        :param doc: path to document
        """
        if proofread:
            path_project = settings.CONVERTED_FILE_LOCATION + 'proofread/'
        else:
            path_project = settings.CONVERTED_FILE_LOCATION + 'translated/'

        cmd = 'libreoffice --convert-to pdf'.split() + [doc] + ['--outdir'] + [path_project]
        p = subprocess.Popen(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        p.wait(timeout=1000)
        stdout, stderr = p.communicate()
        if stderr:
            raise subprocess.SubprocessError(stderr)

    def translate_pdf(self, pdf_file, source_ln="auto", target_ln="en", proofread=False):
        """
        make pdf into word
        translate the word make it into pdf and remove the converted word
        """
        # FILES_DIR = Path(__file__).resolve()
        # file_path = os.path.join(FILES_DIR, pdf_file.my_file.url)
        print(pdf_file.my_file.url)
        pdf_file_name = pdf_file.name
        word_file = target_ln + "_" + pdf_file_name[:-4] + ".docx"
        parse(pdf_file.my_file.path, word_file, start=0, end=None)

        target_word_file = pdf_file_name[:-4] + ".docx"

        number_of_words = language_translation(word_file, target_word_file, source_ln, target_ln)

        if proofread:
            new_pdf_file_name = settings.CONVERTED_FILE_LOCATION + "proofread/" + target_ln + "_" + pdf_file_name
        else:
            new_pdf_file_name = settings.CONVERTED_FILE_LOCATION + "translated/" + target_ln + "_" + pdf_file_name

        try:
            from docx2pdf import convert
            convert(target_word_file, new_pdf_file_name)

        except:
            if proofread:
                self.doc2pdf_linux(target_word_file, proofread=True)
            else:
                self.doc2pdf_linux(target_word_file)

        os.remove(word_file)
        os.remove(target_word_file)
        if proofread:
            return "proofread/" + pdf_file_name, number_of_words
        else:
            return "translated/" + pdf_file_name, number_of_words
