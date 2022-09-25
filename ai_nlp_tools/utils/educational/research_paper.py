from django.conf import settings
import openai

openai.api_key = settings.OPEN_AI_KEY


def research_paper_sections(prmt):
    """
    :param prmt:
    :return: context dist
    """
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt="Expand the research paper title into high-level sections where the title: {}.\n".format(prmt),
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    my_text = response['choices'][0]['text'].split("\n")
    context = {
        'data': [value[2:] for value in my_text]
    }
    return context


def research_paper_section_expander(section, title):
    """
    :param title:
    :param section:
    :return: context dist
    """
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt="Expand the research paper {} section into a detailed professional, witty and clever explanation where "
               "the title: {}.\n".format(section, title),
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    my_text = response['choices'][0]['text'].split("\n\n")
    context = {
        'data': [i for i in my_text if not (i == "" or i == " ")]
    }
    return context
