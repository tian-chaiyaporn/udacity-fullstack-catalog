from flask import render_template, redirect, request, flash, url_for
from catalog import app, session
from db_setup import Item
from authFunctions import login_required, authorization_required


# Edit an item
@app.route('/item/<int:item_id>/edit/', methods=['GET', 'POST'])
@login_required
@authorization_required
def editItem(item_id):
    editedItem = session.query(Item).filter_by(id=item_id).one()
    # only edit item if user has submitted the edit
    if request.method == 'POST':
        if request.form['name'] or request.form['description']:
            editedItem.name = request.form['name']
            editedItem.description = request.form['description']
            flash('Item Successfully Edited %s' % editedItem.name)
            return redirect(url_for('showCategories'))
    # first renders page to edit item
    else:
        return render_template('editItem.html', item=editedItem)
