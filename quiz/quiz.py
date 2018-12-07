#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  quiz.py

from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def hello():
    # return "ELO"
    return render_template
@app.route("/strona")
def strona():
    return "<h1>Witaj na serwerze</h1><h2>Aplikacja !uiz</h2>"

@app.route("/klasa")
def klasa():
    return "<h1>Klasa 3A wita!</h1> "
if __name__ == '__main__':
    app.run(debug=True)
