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
app.config["MONGO_URI"] = os.environ.get('MONGO_URI', '')
app.config['MONG_DBNAME'] = 'ca_rent'
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


@app.route('/dashboard.html')
def figure():
    # Store the entire collection as a list

    # Return the template
    return render_template('dashboard.html')


@app.route('/maps.html')
def plot():
    # Store the entire collection as a list

    # Return the template
    return render_template('maps.html')


@app.route('/contact.html')
def contact():
    # Return the template
    return render_template('contact.html')


@app.route('/data.html')
def data():
    # Return the template
    return render_template('data.html')


@ app.route("/data/all_data")
def get_data():
    all_data_list = list(rent.find())
    return json.dumps(all_data_list, default=json_util.default)


if __name__ == "__main__":
    app.run(debug=True)
