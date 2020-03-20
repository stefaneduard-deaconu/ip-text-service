from flask import Flask, request, jsonify

app = Flask(__name__)

from app import routes

# importing the other packages
from app import ocr

