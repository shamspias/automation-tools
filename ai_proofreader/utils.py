from django.conf import settings

import openai


def ai_proofreading(prompt):
    openai.api_key = settings.OPEN_AI_KEY
    context = {}
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt="Correct this to standard English:\n\n" + prompt,
        temperature=0,
        max_tokens=60,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    context['input'] = prompt
    context['correction'] = response['choices'][0]['text']
    return context
