from flask import Flask, jsonify, redirect, render_template, request, session, url_for ,flash 
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from datetime import timedelta
import os


app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'a_random_secret_key')
app.config['SESSION_TYPE'] = 'filesystem'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB
app.config['SESSION_COOKIE_HTTPONLY'] = True  # Prevents JavaScript from accessing session cookies
app.config['SESSION_COOKIE_SAMESITE'] = 'Lax'  # Helps protect against CSRF attacks
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=365)


@app.route('/')
def index():
    return 'Hello from Flask!'

@app.route('/Research')
def Research():
    return render_template('Research.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')  # Route for the Contact page
def contact():
    return render_template('contact.html')

@app.route('/home')  
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80 ,debug=True)
