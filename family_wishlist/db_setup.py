#!/usr/bin/env python

import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Family(Base):
    __tablename__ = 'family'
    
    id = Column(Integer, primary_key=True)
    family_name = Column(String(250), nullable=False)
    

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    family_id = Column(Integer, ForeignKey('family.id'))
    family = relationship(Family)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return{
            'name': self.name,
            'id' : self.id
        }


class Wishlist(Base):
    __tablename__= 'wishlist'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return{
            'name': self.name,
            'id' : self.id
        }


class Item(Base):
    __tablename__ = 'item'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String(250), nullable=True)
    link = Column(String(250), nullable=True)
    wishlist_id = Column(Integer, ForeignKey('wishlist.id'))
    wishlist = relationship(Wishlist)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return{
            'name': self.name,
            'id' : self.id,
            'wishlist' : self.wishlist
        }

engine = create_engine('sqlite:///familywishlist.db')

Base.metadata.create_all(engine)