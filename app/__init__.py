from flask import Flask, request, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/xscan"
mongo = PyMongo(app)


#
#
# connection_params = {
#     'user': 'stefan',
#     'password': 'EKfBL0RgrrBnSkfB',
#     'host': 'ip-skb3j.mongodb.net',
#     'port': 25058,
#     'namespace': 'test',
# }
# connection = MongoClient(
#     'mongodb://{user}:{password}@{host}:'
#     '{port}/{namespace}'.format(**connection_params)
# )

from app import routes

# importing the other packages
from app import ocr

