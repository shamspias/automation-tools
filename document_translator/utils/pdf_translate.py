from pdf2docx import parse
import os
from .translate_core import language_translation
import subprocess


class TranslatePDF:

    def doc2pdf_linux(self, doc):
        """
        convert a doc/docx document to pdf format (linux only, requires libreoffice)
        :param doc: path to document
        """
        path_project = 'media/files/translate/'
        # cmd = ['libreoffice --convert-to pdf ' + path_project + doc + ' --outdir ' + path_project + file_path]
        cmd = 'libreoffice --convert-to pdf'.split() + [doc] + ['--outdir'] + [path_project]
        print(cmd)
        p = subprocess.Popen(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        p.wait(timeout=1000)
        stdout, stderr = p.communicate()
        if stderr:
            raise subprocess.SubprocessError(stderr)

    def translate_pdf(self, pdf_file, source_ln, target_ln):
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

        language_translation(word_file, target_word_file, source_ln, target_ln)

        new_pdf_file_name = "static_cdn/media_root/translated/" + target_ln + "_" + pdf_file_name
        # try:
        #     from docx2pdf import convert
        #     convert(target_word_file, new_pdf_file_name)
        #     return_pdf_path = "static_cdn/media_root/translated/" + target_ln + "_" + pdf_file_name
        #
        # except:
        #     self.doc2pdf_linux(target_word_file)
        #     return_pdf_path = "static_cdn/media_root/translated/" + pdf_file_name

        from docx2pdf import convert
        convert(target_word_file, new_pdf_file_name)
        return_pdf_path = "static_cdn/media_root/translated/" + target_ln + "_" + pdf_file_name

        os.remove(word_file)
        os.remove(target_word_file)
        return return_pdf_path
