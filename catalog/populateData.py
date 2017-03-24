from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db_setup import Base, Category

# create database session
engine = create_engine('sqlite:///catalogapp.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


# Code taken from vkotovv at https://gist.github.com/vkotovv/6281951
# Clear database everytime this file is run
def clear_data(session):
    meta = Base.metadata
    for table in reversed(meta.sorted_tables):
        print 'Clear table %s' % table
        session.execute(table.delete())
    session.commit()


clear_data(session)


# add 4 categories to database
category_1 = Category(name="Electronic")

session.add(category_1)
session.commit()

category_2 = Category(name="Lights")

session.add(category_2)
session.commit()

category_3 = Category(name="Kitchen Stuff")

session.add(category_3)
session.commit()

category_4 = Category(name="Stationary")

session.add(category_4)
session.commit()


print "added menu items!"
