from django.conf import settings
import openai

openai.api_key = settings.OPEN_AI_KEY


def generate_blog_topics(prompt):
    context = {}
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Generate blog topics on: {}. \n\n 1.".format(prompt),
        temperature=0.7,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    my_text = response['choices'][0]['text'].split("\n")
    context['data'] = [word_value[3:] if word_value[0] != " " else word_value[4:] if i != 0 else word_value[1:] for
                       i, word_value in enumerate(my_text) if word_value != ""]
    return context


def generate_blog_sections(prompt):
    context = {}
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Expand the blog title in to high level blog sections: {} \n\n- Introduction: ".format(prompt),
        temperature=0.6,
        max_tokens=300,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    my_text = response['choices'][0]['text'].split("\n")
    my_text[0] = "- Introduction: "
    context['data'] = [value[2:] for value in my_text]

    return context


def blog_section_expander(prompt, section):
    context = {}
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Blog title {} \n\n."
               "Expand the blog section in to a detailed professional , witty and clever explanation.\n\n {}".format(
            prompt, section),
        temperature=0.7,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    my_text = response['choices'][0]['text'].split("\n")
    context['data'] = [i for i in my_text if not (i == "" or i == " ")]

    return context
