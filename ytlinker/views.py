from ytlinker import app
from ytlinker import ytlib
from flask import render_template
from flask import request


@app.route('/')
def index():
    """Handles index requests
    """
    params = {
        "title" : "YouTube Linker"
    }
    return render_template('index.html', **params)
    

@app.route('/search', methods=['POST'])
def search():
    """Handles search requests
    """
    form = request.form
    linker = ytlib.YTLinkSearch()
    # get for vars
    author = form.get('author')
    filter_string = form.get('filter')
    # perform the search
    feed = linker.search(author, filter_string=filter_string)
    params = {
        "results" : feed.entry,
        "author" : author,
        "filter_string" : filter_string
    }
    return render_template('index.html', **params)