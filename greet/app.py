from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    """Home page."""
    return "Home Page"

@app.route('/welcome')
def welcome():
    """Returns "Welcome"."""
    return "Welcome"

@app.route('/welcome/home')
def welcome_home():
    """Returns "Welcome home"."""
    return "Welcome home"

@app.route('/welcome/back')
def welcome_back():
    """Returns "Welcome back"."""
    return "Welcome back"