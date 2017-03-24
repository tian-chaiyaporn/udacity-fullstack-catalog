from flask import render_template, redirect, request, flash, url_for
from catalog import app, session
from db_setup import Item
from authFunctions import login_required, authorization_required


# Delete an item
@app.route('/item/<int:item_id>/delete/', methods=['GET', 'POST'])
@login_required
@authorization_required
def deleteItem(item_id):
    itemToDelete = session.query(Item).filter_by(id=item_id).one()
    # only delete item after user confirms with a POST method
    if request.method == 'POST':
        session.delete(itemToDelete)
        flash('%s Successfully Deleted' % itemToDelete.name)
        session.commit()
        return redirect(url_for('showCategories', item_id=item_id))
    # shows a confirmation page whether user wants to delete
    else:
        return render_template('deleteItem.html', item=itemToDelete)
