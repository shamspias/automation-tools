from django.conf import settings

import openai


def ai_proofreading(prompt):
    openai.api_key = settings.OPEN_AI_KEY
    context = {}
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt="Correct this to standard English:\n\n" + prompt + " \n\n",
        temperature=0,
        max_tokens=500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    context['input'] = prompt
    my_text = response['choices'][0]['text']
    context['correction'] = my_text.split('\n')
    while "" in context['correction']:
        context['correction'].remove("")
    return context
