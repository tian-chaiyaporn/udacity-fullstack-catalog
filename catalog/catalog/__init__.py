from flask import Flask
from flask import session as login_session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# create Flask app
app = Flask(__name__)
Base = declarative_base()


def connect(user, password, db, host='localhost', port=5432):
    url = 'postgresql://{}:{}@{}:{}/{}'
    url = url.format(user, password, host, port, db)
    # The return value of create_engine() is our connection object
    engine = sqlalchemy.create_engine(url, client_encoding='utf8')
    # We then bind the connection to MetaData()
    meta = sqlalchemy.MetaData(bind=engine, reflect=True)
    return engine, meta


# Connect to Database and create database session
engine, meta = connect('catalog', '', 'catalog_app')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

'''
Imports are made after creating session, app
'''

import db_setup

# homepage and showing items -> url = (/)
import catalog.readData

# create new item -> url = (/item/new)
import catalog.createItem

# edit item -> url = (/item/<item_id>/edit)
import catalog.editItem

# delete item -> url = (/item/<item_id>/delete)
import catalog.deleteItem

# show API with JSON -> url = (/item/JSON)
import catalog.JSONapi

# fb auth functions -> url =(/fbconnect) & (/fbdisconnect)
import catalog.fbAuth

# login token -> url = (/login)
import catalog.loginToken
