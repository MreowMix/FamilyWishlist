#!/usr/bin/env python

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Family, User, Wishlist, Item

engine = create_engine('sqlite:///familywishlist.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Create Initial Families
Family1 = Family(family_name='Jon Family', id='0')
session.add(Family1)
session.commit()

Family2 = Family(family_name='Kelly-Visser', id='1')
session.add(Family2)
session.commit()

# Create Initial User
User1 = User(name='AdminUser', email='admin@user.me')
session.add(User1)
session.commit()

User2 = User(name='RegularUser', email='regular@user.me')
session.add(User2)
session.commit()

print "Done!"