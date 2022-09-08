'''
Date: 2022-03-25 20:20:08
LastEditors: Azus
LastEditTime: 2022-03-29 16:24:40
FilePath: /KDS/backend/app.py
'''
from re import template
from flask import Flask, render_template 
import reverseProxy as rP
app=Flask(__name__, template_folder='templates' )
# app=Flask(__name__)

ENV = "prds"
DEV_SERVER_URL = 'http://localhost:3000/'

@app.route('/')
def index():
#     if ENV == "dev":
#         return rP.proxyRequest(DEV_SERVER_URL, "")
#     else:
#         return render_template('index.html')
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Predict 
    return

if __name__ == '__main__':
    app.run(debug=True)