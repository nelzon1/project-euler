# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 19:23:45 2018

@author: jaken
"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

app.run()