from flask import Flask, request
app = Flask(__name__)


@app.route('/')
def homepage():
    return f'<h1> Welcome Page </h1>'

@app.route('/welcome')
def welcome():
    return f'<h1> Welcome </h1>'

@app.route('/welcome/home')
def welcome_home():
    return f'<h1> Welcome home </h1>'
    
@app.route('/welcome/back')
def welcome_back():
    return f'<h1> Welcome back </h1>'