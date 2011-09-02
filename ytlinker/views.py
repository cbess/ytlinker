# -*- coding: utf-8 -*-
from ytlinker import app
from ytlinker import ytlib
from flask import render_template, request, url_for, session
from ytlinker import utils


@app.route('/static/*')
def static_files():
    """Handles static files requests
    """
    endswith = request.path.endswith
    if endswith('main.css'):
        return url_for('static', filename='css/main.css')
    return ''
    

@app.route('/')
def index():
    """Handles index requests
    """
    response = {
        "title" : u"Welcome"
    }
    return render_template('index.html', **response)
    

@app.route('/search', methods=['POST', 'GET'])
def search():
    """Handles search requests
    """
    # get form vars
    if request.method == 'POST':
        form = request.form
    else:
        form = request.args
    author = form.get('author')
    filter_string = form.get('filter')
    # perform the search
    linker = ytlib.YTLinkSearch()
    feed = linker.search(author, filter_string=filter_string)
    search_list = utils.store_search(author, filter_string)
    # build response
    response = {
        "results" : feed.entry,
        "author" : author,
        "filter_string" : filter_string,
        "title" : u"%s - YT Search" % filter_string,
        "searches" : session['searches']
    }
    return render_template('index.html', **response)
