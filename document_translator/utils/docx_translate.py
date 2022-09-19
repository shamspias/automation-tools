from .translate_core import language_translation


class TranslateDocx:
    def translate_docx(self, doc_file, source_ln, target_ln):
        """
        translate the word
        """
        doc_file_name = doc_file.name
        word_file = target_ln + "_" + doc_file_name
        new_docx_file_name = "static_cdn/media_root/translated/" + word_file
        language_translation(doc_file.my_file.path, new_docx_file_name, source_ln, target_ln)

        return "translated/" + word_file
