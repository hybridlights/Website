#!/bin/python3

from flask import Flask, request, Response, render_template, redirect 
from dotenv import load_dotenv
import os

load_dotenv()

VERSION = '0.0.1'



app = Flask(__name__, static_folder='static', template_folder='static/templates')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')


@app.context_processor
def load_jinja_vars():
    return {
        'version': VERSION
    }


@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('content/imgs/favicon_temp.ico')


@app.route('/')
def root():
    return redirect('/index.html', code=302)

@app.route('/index.html')
def index():
    return render_template('index.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')




if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=int(os.environ.get('PORT', 5000)),
        debug=True
    )