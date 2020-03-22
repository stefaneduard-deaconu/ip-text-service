from app import app
from app.ocr import translate

# Deocamdata, DE FOLOSIT DOAR PENTRU A TESTA FUNCTIONALITATI
# here we only keep the routes for the ocr, so we need to import all the functions from ocr
@app.route('/ocr', methods=['GET'])
def ocr():
    translation = translate('This is where OCR magic happens.')
    return f"""
    <h1>This is where OCR magic happens.</h1>
    can be translated to
    <h1>{translation}</h1>
    """
