#!/usr/bin/env python3

from flask import Flask, request, Response, render_template, redirect, flash, get_flashed_messages, jsonify
from dotenv import load_dotenv
from pprint import pprint
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
    return app.send_static_file('assets/imgs/favicon_temp.ico')


@app.route('/')
def root():
    return redirect('/home', code=301)

@app.route('/home')
def index():
    return render_template('home.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html')


@app.route('/verhuur')
def verhuur():
    flash('Deze pagina is nog in ontwikkeling')
    return redirect('/home', code=302)
    return render_template('verhuur.html')


@app.route('/get-flashed-messages', methods=['GET', 'POST'])
def flash_messages():

    options = [
        'with-categories',
        'category-filter'
    ]

    if request.args:
        kwargs = dict(request.args)
    else:
        kwargs = dict()

    if request.headers:
        for key, value in dict(request.headers).items():
            key = key.lower()
            if key in options:
                kwargs[key.replace('-', '_')] = value

    if kwargs.get('with_categories'):
        flash_messages = []
        for category, message in get_flashed_messages(**kwargs):
            flash_messages.append({'message': message, 'category': category})
            # TODO: add proper logging
            pprint(flash_messages)
        
        return jsonify(flash_messages)

    return jsonify(get_flashed_messages(**kwargs))





if __name__ == '__main__':
    app.run(
        host=os.environ.get('HOST_IP', '0.0.0.0'),
        port=int(os.environ.get('PORT', 5000)),
        debug=True
    )