import pytesseract
from googletrans import Translator
translator = Translator(service_urls=[
    'translate.google.com',
    'translate.google.co.uk'
])


# TODO remove this function, it is only for showing how a function may work, and used in the only route from routes :)
# sample function:
def translate(text, dest='ro', src='en'):
    translation = translator.translate(text, dest=dest, src=src)
    return translation.text


# TODO the next function must apply tesseract to extract the text from the image formated as base64 (str)
# TODO and it will return the entire text
def extract_text(img_base64, img_type):
    pass


# TODO the next function uses the translator to translate the given text and return the result
def translate_text(text, dest='ro', src='en'):
    pass


# importing the routes for the ocr package
from app.ocr import routes  # we use this to import all the necessary routes to the main app
