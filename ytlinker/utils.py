from flask import session


def store_search(author, search_string):
    """Stores the author and search string in the user session
    :return: List of search strings for the specified author
    """
    if not session.get('searches'):
        session['searches'] = dict()
    # try to grab the author searches
    search_list = session['searches'].get(author)
    if not search_list:
        search_list = [search_string]
    else:
        # don't duplicate search entries
        if search_string not in search_list:
            search_list.append(search_string)
    session['searches'][author] = search_list
    session.modified = True
    return search_list
