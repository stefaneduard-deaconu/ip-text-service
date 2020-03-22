from app import app
from app import mongo


@app.route('/')
@app.route('/index')
def index():
    return '''
    <h1> Welcome to the text service <h1>
    '''