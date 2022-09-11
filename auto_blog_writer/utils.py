from django.conf import settings
import openai

openai.api_key = settings.OPEN_AI_KEY


def generate_blog_topics(prompt):
    context = {}
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Generate blog topics on: {}. \n \n ".format(prompt),
        temperature=0.7,
        max_tokens=500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    context['action'] = "/ai-blog/sections/"
    context['input'] = prompt
    context['name'] = "Main Topic"
    context['correction'] = response['choices'][0]['text']
    return context


def generate_blog_sections(prompt, title):
    context = {}
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Expand the blog title: {} \n in to high level blog sections: {} \n\n -Introduction:".format(prompt,
                                                                                                            title),
        temperature=0.6,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    context['action'] = "/ai-blog/sections/expander/"
    context['input'] = prompt
    context['name'] = "Sections"
    context['correction'] = response['choices'][0]['text']
    return context


def blog_section_expander(prompt, section):
    context = {}
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Expand the blog section: {} \n\n in to a detailed professional , witty and clever explanation.\n\n {}".format(
            prompt, section),
        temperature=0.7,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    context['input_parent'] = section
    context['input'] = prompt
    context['correction'] = response['choices'][0]['text']
    return context
