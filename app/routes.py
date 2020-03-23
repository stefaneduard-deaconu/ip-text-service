from app import app
from app import mongo
from flask import render_template_string, request
import requests

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

@app.route('/docs',methods=['POST'])
def create_doc():
    req_data = request.get_json()
    docs = req_data.get('docs')
    user_id = req_data('userId')
    #  lucram cu db
    db_docs = mongo.db.docs.find({"user_id": user_id})
    db_docs_ids = [doc.doc_id for doc in db_docs]
    docs_new = [doc for doc in docs if doc.get('doc_id') not in db_docs_ids]
    docs_update = [doc for doc in docs if doc.get('doc_id') in db_docs_ids]
    mongo.db.docs.insert_many(docs_new)
    for doc in docs_update:
        myquery = {"doc_id": doc.doc_id}
        newvalues = {"$set": doc}
        mongo.db.docs.update_one(myquery, newvalues)
    #
    return '{ "error": false }'


@app.route('/docs',methods=['DELETE'])
def delete_doc():
    req_data = request.get_json()
    user_id = req_data.get('userId')
    #
    mongo.db.docs.delete_many({"user_id": user_id})
    #
    return '{ "error": false }'


@app.route('/docs/<user_id>', methods=['POST'])
def create_doc(user_id):
    req_data = request.get_json()
    doc = req_data.get('doc')
    doc = {**doc, 'user_id': user_id}
    #
    mongo.db.docs.insert_one(doc)
    #
    return '{ "error": false}'



@app.route('/docs/<user_id>', methods=['PUT'])
def update_doc(user_id):
    req_data = request.get_json()
    doc_id = req_data.get('docId')
    doc = req_data.get('doc')
    #
    mongo.db.docs.update_one(
        {"docId": doc_id, "userId": user_id}, doc)

    #
    return '{ "error": false}'



@app.route('/docs/<user_id>', methods=['DELETE'])
def delete_doc(user_id):
    req_data = request.get_json()
    doc_id = req_data.get('docId')
    #
    mongo.db.docs.delete_one(
        {'docId': doc_id, 'userId': user_id}
    )
    #
    return '{ "error": false}'




