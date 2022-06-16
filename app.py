from flask import Flask, render_template
import requests
import jinja2
import json


app = Flask(__name__)

@app.route('/', methods=['GET'])

def index():
    req = requests.get("https://api.thecatapi.com/v1/breeds")

    headers = {'x-api-key': 'api_key=6fb0d3d2-9e3c-4dbc-bdfa-065b2b907da7'}
    data = json.loads(req.content)

   
    return render_template('index.html', data=data)