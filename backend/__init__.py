'''
Date: 2022-03-25 20:20:08
LastEditors: Azus
LastEditTime: 2022-03-26 22:12:30
FilePath: /react-ml-app/backend/__init__.py
'''
import os
from tkinter import image_types
from flask import Flask, request, render_template, jsonify
from PIL import Image

'''
Date: 2022-03-26 16:49:36
LastEditors: Azus
LastEditTime: 2022-03-26 16:49:43
FilePath: /react-ml-app/backend/reverseProxy.py
'''
# backend/reverseProxy.py

from requests import get

# Simple reverse proxy for use with webpack-dev-server.
def proxyRequest(host, path):
    response = get(host + path)

    excluded_headers = [
        "content-encoding",
        "content-length",
        "transfer-encoding",
        "connection",
    ]
    headers = {
        name: value
        for name, value in response.raw.headers.items()
        if name.lower() not in excluded_headers
    }
    return (response.content, response.status_code, headers)


MODE = os.getenv('FLASK_ENV')
DEV_SERVER_URL = 'http://localhost:3000/'


app = Flask(__name__)


def create_app():
    # app = Flask(__name__)
    # MODE = os.getenv('FLASK_ENV')
    # DEV_SERVER_URL = 'http://localhost:3000/'
    app = Flask(__name__,template_folder="templates",static_folder="static",static_url_path="/backend/static")
    # Ignore static folder in development mode.
    # if MODE == "development":
        # app = Flask(__name__, static_folder=None)
    # app = Flask(__name__, static_folder=None)
    return app

# @app.route('/')
# @app.route('/<path:path>')
# def index(path=''):
#     # if MODE == 'development':
#     return proxyRequest(DEV_SERVER_URL, path)
#     # else:
#     #     return render_template("index.html")    

@app.route('/')
def index():
    return render_template("index.html")



@app.route('/api/upload', methods=['POST'])
def handle_form():
    files = request.files
    file = files.get('file')
    image= request.files.get('file')
    if image is not None:
        image.save('./')

    """
    CODE TO HANDLE FILE
    """
    # return jsonify({
    #     'success': True,
    #     'file': 'Received'
    # })
    return render_template('index.html')




