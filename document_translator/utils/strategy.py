from pdf2docx import parse


# PDF to Word
def pdf_to_docx(pdf_file, word_file):
    """
    Convert PDF to Docx using pdf2docx
    :param pdf_file:
    :param word_file:
    :return: File(docx)
    """
    return parse(pdf_file.my_file.path, word_file, start=0, end=None)


# PDF to HTML
def pdf_to_html(pdf_file, html_file):
    """
    :param pdf_file:
    :param html_file:
    :return: File(HTML)
    """
    return Convert.ToHtml(pdf_file, html_file)
# Word to PDF

# Word to HTML

# HTML to PDF

# HTML to Word


# Audio to Text

# Video to Text
