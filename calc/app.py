from operations import add, sub, mult, div
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    """Home page."""
    return "Page Loaded"

@app.route('/add')
def add_nums():
    """Add a and b."""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = str(add(a,b))
    return f"{a} + {b} = {result}"

@app.route('/sub')
def sub_nums():
    """Subtract a and b."""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = str(sub(a,b))
    return f"{a} - {b} = {result}"

@app.route('/mult')
def mult_nums():
    """Subtract a and b."""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = str(mult(a,b))
    return f"{a} * {b} = {result}"

@app.route('/div')
def div_nums():
    """Subtract a and b."""
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = str(div(a,b))
    return f"{a} / {b} = {result}"

