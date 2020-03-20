import pytesseract
from googletrans import Translator
translator = Translator(service_urls=[
    'translate.google.com',
    'translate.google.co.uk'
])


# TODO here we'll have the functions for working with the text
# sample function:
def translate(text, dest='ro', src='en'):
    translation = translator.translate(text, dest=dest, src=src)
    return translation.text


# importing the routes for the ocr package
from app.ocr import routes  # we use this to import all the necessary routes to the main app
