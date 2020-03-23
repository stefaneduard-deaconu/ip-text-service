from app import app
from app import mongo
from flask import render_template_string

@app.route('/')
@app.route('/index')
def index():
    db = mongo.db
    docs = db.docs.find({})
    imgs = db.imgs.find({})
    return render_template_string(
        '''
            <h1> Welcome to the text service <h1>
            <div>{{ db }}</div>
            <h2> These are the docs </h2>
            {% for doc in docs %}
            <div>{{ doc }}</div>
            {% endfor %}
            <h2> Below are the images </h2>
            {% for img in imgs %}
            <div>{{ img }}</div>
            {% endfor %}
        ''',
        db=db,
        docs=docs,
        imgs=imgs
    )
