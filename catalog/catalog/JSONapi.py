from flask import jsonify
from catalog import app, session
from db_setup import Item, Category


# JSON APIs to view Item Information
@app.route('/item/JSON')
def itemsJSON():
    items = session.query(Item)
    print items
    # get all items with category names from both Item and Category tables
    results = session.query(Item, Category).join(Category)
    # for each items, return a serialized JSON
    return jsonify(items=[serialize_JSON(r) for r in results])


# Return object data in easily serializeable format
def serialize_JSON(r):
    return {
        'item_name': r.Item.name,
        'description': r.Item.description,
        'id': r.Item.id,
        'category': r.Category.name,
        'time_created': r.Item.time_created,
    }
