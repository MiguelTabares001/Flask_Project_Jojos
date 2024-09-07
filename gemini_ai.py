import os
import pathlib

import markdown
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown


def to_markdown(text):
  text = text.replace('•', '  *')
  return markdown.markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

GOOGLE_API_KEY=os.getenv('GOOGLE_API_KEY')

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-1.5-flash')

#Funcion

def generate_prompt(prompt):
  response = model.generate_content(prompt)
  response.text
  return (response.text)





