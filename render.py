# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 14:12:16 2018

@author: Akshay Rajaraman
"""
from flask import Flask,render_template,request
import json
app = Flask(__name__)
@app.route("/")
#def index(name=None):
#    return render_template('JHacks.html', name=name)

def index(name=None):
    return render_template('JHacks.html', name=name)

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['JSON']
    processed_text = text
    parsed_json = json.loads(processed_text)
    nodeDataArray_json = parsed_json['nodeDataArray']
    category_string = ""
    for i in nodeDataArray_json:
        category_string = category_string+ i['category']+" "+i['text']+" "+str(i['key'])+" "
    
    return category_string
    
if __name__=="__main__":
    app.run()