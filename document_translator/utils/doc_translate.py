from .translate_core import language_translation


def translate_doc(doc_file, source_ln, target_ln):
    """
    translate the word
    """
    doc_file_name = doc_file.name
    word_file = target_ln + "_" + doc_file_name
    new_docx_file_name = "media/files/" + word_file
    language_translation(doc_file.my_file.path, new_docx_file_name, source_ln, target_ln)

    return "files/" + word_file
