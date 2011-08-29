from ytlinker import app
from flask import render_template

@app.route('/')
def index():
    """Handles index requests
    """
    params = {
        "title" : "YouTube Linker"
    }
    return render_template('index.html', **params)