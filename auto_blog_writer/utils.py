from django.conf import settings
import openai

openai.api_key = settings.OPEN_AI_KEY


def generate_blog_topics(prompt):
    context = {}
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Generate blog topics on: {}. \n\n".format(prompt),
        temperature=0.7,
        max_tokens=500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    context['input'] = prompt
    my_text = response['choices'][0]['text']
    context['topics'] = my_text.split("\n")
    return context


def generate_blog_sections(prompt):
    context = {}
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Expand the blog title in to high level blog sections: {} \n\n- Introduction: ".format(prompt),
        temperature=0.6,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    context['input'] = prompt
    my_text = response['choices'][0]['text']
    context['sections'] = my_text.split("\n")
    context['sections'][0] = "- Introduction"
    return context


def blog_section_expander(prompt, section):
    context = {}
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Blog topic {} \n\n."
               "Expand the blog section in to a detailed professional , witty and clever explanation.\n\n {}".format(
            prompt, section),
        temperature=0.7,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    context['input_parent'] = section
    context['input'] = prompt
    # my_text = response['choices'][0]['text']
    # context['section_details'] = my_text.split("\n")
    context['section_details'] = response['choices'][0]['text']
    return context
