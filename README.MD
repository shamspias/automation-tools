# Automation Tools

## Make Life Easy Work Faster

### Technology

> Programming Language

- Python3

> Framework

- Django
- Django REST framework

> Libraries

- [Deep_translator](https://pypi.org/project/deep-translator/)
- [Pdf2docx](https://pypi.org/project/pdf2docx/)
- [Beautifulsoup4](https://pypi.org/project/beautifulsoup4/)
- [pypandoc](https://pypi.org/project/pypandoc/)

> Tools

- GPT-3

### Automated Tools

- Translate Documents with multiple Translator
- Proofreading with GPT-3 davinci model
- Automatic Blog Maker with GPT-3 davinci model

### Installation

#### First Create a Virtual Environment

> Windows

- Make sure you have python installed on your pcopen cmd or PowerShell

  `python -m venv  yourvenv`

> Linux and MAC

- Open terminal

```
sudo apt-get install python3-pip
sudo apt-get install python3-venv
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