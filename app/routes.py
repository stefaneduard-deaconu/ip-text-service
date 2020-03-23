from app import app
from app import mongo


@app.route('/')
@app.route('/index')
def index():
    return f'''
    <h1> Welcome to the text service <h1>
    <div>{mongo.db.list_collection_names()}</div>
    '''