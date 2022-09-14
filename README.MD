# Automation Tools

## Boost Your Work With Automation

### Automated Tools

- Translate Documents with multiple Translator
- Proofreading with GPT-3 davinci model
- Automatic Blog Maker with GPT-3 davinci model

### Technology

> Programming Language

- Python3

> Framework

- Django
- Django REST framework

> Libraries

- [OpenAI](https://pypi.org/project/openai/)
- [Deep_translator](https://pypi.org/project/deep-translator/)
- [Pdf2docx](https://pypi.org/project/pdf2docx/)
- [Beautifulsoup4](https://pypi.org/project/beautifulsoup4/)
- [pypandoc](https://pypi.org/project/pypandoc/)
- [pdfkit](https://pypi.org/project/pdfkit/)
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)

> Tools

- GPT-3

### Installation

#### Download and Install Additional Software

#### 1. pdfkit
> Windows

- Download link: [WKHTMLTOPDF](https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.4/wkhtmltox-0.12.4_msvc2015-win64.exe)
- Set: PATH variable set binary folder in Environment variables.

> Linux
- `sudo apt-get install wkhtmltopdf -y`

#### 2. pypandoc
- [Installation Process](https://pandoc.org/installing.html)

#### Create a Virtual Environment

> Windows

- Make sure you have python installed on your pcopen cmd or PowerShell

  `python -m venv  yourvenv`

> Linux and MAC

- Open terminal

```
sudo apt-get install python3-pip -y && sudo apt-get install python3-venv -y
```

After that just type

`python3 -m venv yourvenv`

#### Activate Virtual Environment.

> Windows

`yourvenv/Scripts/activate`

- If show any error then open Powershell in admin
  then type

`Set-ExecutionPolicy -ExecutionPolicy RemoteSigned`
and press "A" then Enter.

> Linux

`. yourvenv/bin/activate`

- Install the requirement.txt

> Windows

`pip install -r requirement.txt`

> Linux

`pip3 install -r requirement.txt`

### RUN

`python manage.py runserver ip:port`

- Example

`python manage.py runserver 0.0.0.0:8000`