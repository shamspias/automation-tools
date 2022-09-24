from django.conf import settings
import openai

openai.api_key = settings.OPEN_AI_KEY


def normal_research_paper(prmt):
    """
    :param prmt:
    :return: context dist
    """
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt="Make a research paper where the topic: {}".format(prmt),
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    my_text = response['choices'][0]['text']
    context = {'data': [my_text]}
    return context
