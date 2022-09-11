import pypandoc
from bs4 import BeautifulSoup
import re
import os
from deep_translator import (GoogleTranslator,
                             MicrosoftTranslator,
                             PonsTranslator,
                             LingueeTranslator,
                             MyMemoryTranslator,
                             YandexTranslator,
                             PapagoTranslator,
                             DeeplTranslator,
                             QcriTranslator,
                             single_detection,
                             batch_detection)


def language_translation(source_doc, target_doc, source_lan="auto", target_lan="de"):
    """
    To translate Language
    return docx file
    """
    source = source_doc.strip()
    source_language = source_lan.strip()
    target = target_doc.strip()
    target_language = target_lan.strip()

    output = pypandoc.convert_file(source, 'html5')

    soup = BeautifulSoup(output, features="lxml")

    target_tags = re.findall(r'<.+?>', output)  # get all html tags
    target_tags = list(dict.fromkeys(target_tags))  # removing duplicates

    for i, word in enumerate(target_tags):
        target_tags[i] = word.replace('</', '<')
        target_tags[i] = target_tags[i].replace('<', '')
        target_tags[i] = target_tags[i].replace('>', '')

        if " " in target_tags[i]:
            target_tags[i] = target_tags[i][:target_tags[i].index(" ")]

    target_tags = list(dict.fromkeys(target_tags))  # removing duplicates

    for i in soup.findAll(target_tags):
        try:
            i.string.replace_with(GoogleTranslator(source=source_language, target=target_language).translate(i.string))
        except:
            print("")

    with open("output1.html", "w") as file:
        file.write(str(soup))

    pypandoc.convert_file('output1.html', 'docx', outputfile=target)
    os.remove("output1.html")

    print("Document translation is completed.")
    return True
