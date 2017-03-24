from flask import render_template
from catalog import app, session
from db_setup import Category, Item
from sqlalchemy import desc
from authFunctions import login_required


# Show only Categories in homepage
@app.route('/')
@login_required
def showCategories():
    categories = session.query(Category).order_by(desc(Category.name))
    return render_template('category.html', categories=categories)


# When a category is clicked, this function is called to show items in that
# category
@app.route('/<int:category_id>/', methods=['GET', 'POST'])
def showCategoryItems(category_id):
    items = session.query(Item).filter_by(cat_id=category_id)
    return render_template('items.html', items=items)


# When an item is clicked, this function is called to show details in that
# item
@app.route('/item/<int:item_id>/', methods=['GET'])
def showItem(item_id):
    item = session.query(Item).filter_by(id=item_id).one()
    return render_template('itemDetail.html', item=item)
