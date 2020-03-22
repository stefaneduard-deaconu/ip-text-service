from flask import Flask, request, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/Database"
mongo = PyMongo(app)

from app import routes

# importing the other packages
from app import ocr

