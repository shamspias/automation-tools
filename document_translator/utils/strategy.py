import pypandoc
import os
import speech_recognition as sr
from pdf2docx import parse
import deep_translator as dt


# PDF to Word
def pdf_to_docx(pdf_file, word_file):
    """
    Convert PDF to Docx using pdf2docx
    :param pdf_file:
    :param word_file:
    :return: File(docx)
    """
    return parse(pdf_file.my_file.path, word_file, start=0, end=None)


# Word to PDF

# Word to HTML
def word_to_html(word_file, html_file=None):
    if not html_file:
        return pypandoc.convert_file(word_file, 'html5')
    else:
        return pypandoc.convert_file(word_file, 'html5', outputfile=html_file)


# HTML to Word
def html_to_word(html_file, word_file=None):
    if not word_file:
        return pypandoc.convert_file(html_file, 'docx')
    else:
        return pypandoc.convert_file(html_file, 'docx', outputfile=word_file)


# Audio to Text
def audio_to_text(audio_file, duration=None, language=None):
    """
    :param duration:
    :param language:
    :param audio_file:
    :return: string
    """
    audio_file_wav = audio_file[:4] + ".wav"
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
            text = r.recognize_google(audio_data, language=language)
        else:
            text = r.recognize_google(audio_data)
    return text


# Video to Text
def video_to_text(video_file, duration=None, language=None):
    """
    :param video_file:
    :param duration:
    :param language:
    :return: String
    """
    video_as_mp3 = video_file[:4] + ".mp3"
    command2mp3 = "ffmpeg -i {} {}".format(video_file, video_as_mp3)
    os.system(command2mp3)
    return audio_to_text(video_as_mp3, duration, language)


# Translate String
def translate_strings(text, source_lan="auto", target_lan="de", translator_engine=dt.GoogleTranslator):
    """
    :param translator_engine:
    :param text:
    :param source_lan:
    :param target_lan:
    :return: String
    """
    return translator_engine(source=source_lan, target=target_lan).translate(text)
