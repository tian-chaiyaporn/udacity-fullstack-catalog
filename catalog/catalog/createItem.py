from flask import render_template, redirect, request, flash, url_for
from catalog import app, session
from db_setup import Category, Item
from authFunctions import login_required


# Create a new item
@app.route('/item/new/', methods=['GET', 'POST'])
@login_required
def addItem():
    # only add item if user has submitted the item details
    if request.method == 'POST':
        newItem = Item(name=request.form['name'],
                       description=request.form['description'],
                       cat_id=request.form['cat_id'])
        session.add(newItem)
        flash('New Item %s Successfully Created' % newItem.name)
        session.commit()
        return redirect(url_for('showCategories'))
    # first renders page to add item
    else:
        categories = session.query(Category)
        return render_template('newItem.html', categories=categories)
