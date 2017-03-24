from flask import redirect, flash
from catalog import login_session, session
from db_setup import Item
from functools import wraps


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Redirect users to login page if not logged in
        if 'username' not in login_session:
            return redirect('/login')
        return f(*args, **kwargs)
    return decorated_function


def authorization_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Redirect users to login page if not logged in
        item_id = kwargs['item_id']
        author = session.query(Item).filter_by(id=item_id).one()
        if login_session['user_id'] == author.id:
            flash("Only author is allowed to edit and delete items")
            url = '/item/%s' % (author.id)
            print url
            return redirect(url)
        return f(*args, **kwargs)
    return decorated_function
