#!/usr/bin/env python3

from flask import Flask, request, Response, render_template, redirect, flash
from dotenv import load_dotenv
import os

load_dotenv()



VERSION = os.environ.get('VERSION')

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
    return redirect('/home', code=302)

@app.route('/home')
def index():
    return render_template('index.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html')


@app.route('/verhuur')
def verhuur():
    return render_template('verhuur.html')



if __name__ == '__main__':
    app.run(
        host=os.environ.get('HOST_IP', '0.0.0.0'),
        port=int(os.environ.get('PORT', 5000)),
        debug=True
    )