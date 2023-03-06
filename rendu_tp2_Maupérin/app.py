#!/usr/bin/env python3
"""use_of_templates/app.py
Develop the power of Flask and Jinja by creating HTML templates,
expending those templates, and pass variable to create dynamic content.
"""

import datetime  # import a library to manage dates

import flask  # import the flask library
from flask import request

app = flask.Flask(__name__)  # instantiate a minimal webserver


@app.route('/')  # create the index route
def index():
    # we moved the HTML inside the 'templates/' directory
    # the documentation for the template engine is available here:
    # https://jinja.palletsprojects.com/

    return flask.render_template('index.html')


@app.route('/review/', methods=['POST', 'GET'])  # create a new route
def review():
    return flask.render_template('review.html')

@app.route('/avis/', methods=['POST'])  # create a new route
def avis():
    nom=request.form['nom']
    email=request.form['email']
    avis=request.form['avis']
    return flask.render_template('avis.html', nom=nom, email=email, avis=avis)


if __name__ == '__main__':  # consider this line as the main
    app.run('0.0.0.0', 8080, debug=True)  # start web server in debug mode on port 8080
