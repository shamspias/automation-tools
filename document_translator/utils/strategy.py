import pypandoc
import os
import speech_recognition as sr
from pdf2docx import parse
import deep_translator as dt
import subprocess

import datetime


class Strategy:
    # PDF to Word
    def pdf_to_docx(self, pdf_file, word_file):
        """
        Convert PDF to Docx using pdf2docx
        :param pdf_file:
        :param word_file:
        :return: File(docx)
        """
        return parse(pdf_file.my_file.path, word_file, start=0, end=None)

    # Word to PDF
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

    def word_to_pdf(self, word_file, pdf_file, save_pdf_location):
        try:
            from docx2pdf import convert
            convert(word_file, pdf_file)
            return_pdf_path = save_pdf_location
            return return_pdf_path

        except:
            self.doc2pdf_linux(doc=word_file)
            return_pdf_path = save_pdf_location
            return return_pdf_path

    # Word to HTML
    def word_to_html(self, word_file, html_file=None):
        if not html_file:
            return pypandoc.convert_file(word_file, 'html5')
        else:
            return pypandoc.convert_file(word_file, 'html5', outputfile=html_file)

    # HTML to Word
    def html_to_word(self, html_file, word_file=None):
        if not word_file:
            return pypandoc.convert_file(html_file, 'docx')
        else:
            return pypandoc.convert_file(html_file, 'docx', outputfile=word_file)

    # Audio to Text
    def audio_to_text(self, audio_file, duration=None, language=None):
        """
        :param duration:
        :param language:
        :param audio_file:
        :return: string
        """
        if not audio_file.name.endswith(".mp3"):
            audio_file_mp3 = audio_file.name[:4] + ".mp3"
            command2mp3 = "ffmpeg -i {} {}".format(audio_file, audio_file_mp3)
            os.system(command2mp3)
        if audio_file.name.endswith(".wav"):
            audio_file_wav = audio_file
        else:
            audio_file_wav = audio_file.name[:4] + ".wav"
            command2wav = "ffmpeg -i {} {}".format(audio_file, audio_file_wav)
            os.system(command2wav)

        r = sr.Recognizer()

        with sr.AudioFile(audio_file_wav) as source:
            # listen for the data (load audio to memory)
            if duration:
                audio_data = r.record(source, duration=duration)
            else:
                audio_data = r.record(source)
            if language:
                text = r.recognize_google(audio_data, language=language, show_all=True)
            else:
                text = r.recognize_google(audio_data, show_all=True)
                print(text)

        return text["alternative"][0]["transcript"]

    # Video to Text
    def video_to_text(self, video_file, duration=None, language=None):
        """
        :param video_file:
        :param duration:
        :param language:
        :return: String
        """
        video_as_mp3 = video_file.name[:4] + ".mp3"
        command2mp3 = "ffmpeg -i {} {}".format(video_file, video_as_mp3)
        os.system(command2mp3)
        return self.audio_to_text(audio_file=video_as_mp3, duration=duration, language=language)

    # Translate String
    def translate_strings(self, text, source_lan="auto", target_lan="de", translator_engine=dt.GoogleTranslator):
        """
        :param translator_engine:
        :param text:
        :param source_lan:
        :param target_lan:
        :return: String
        """
        return translator_engine(source=source_lan, target=target_lan).translate(text)
