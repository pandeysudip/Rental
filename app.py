from flask import Flask, request, render_template, redirect, jsonify
import json
import os
from model_param import model_load
from bson import json_util
from pymongo import MongoClient
from flask_pymongo import PyMongo

# Create an instance of Flask
app = Flask(__name__)

# Use PyMongo to establish Mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/ca_rent"
mongo = PyMongo(app)

# Creating collection 
rent = mongo.db['rent']

# Defining route 
@app.route('/')
def home():
    # Return the template
    return render_template('index.html')

@app.route('/index.html')
def index():
    # Return the template
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
