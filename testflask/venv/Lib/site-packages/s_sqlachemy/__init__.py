import types
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, Float
from sqlalchemy import update
import sqlalchemy
from sqlalchemy import event, inspect, orm
from copy import deepcopy
import time

__version__ = '0.11'

def current_time():
    return int(time.time())


def _include_sqlalchemy(obj):
    for module in sqlalchemy, sqlalchemy.orm:
        for key in module.__all__:
            if not hasattr(obj, key):
                setattr(obj, key, getattr(module, key))


class ModelMixin(object):
    id = Column(Integer, primary_key=True)
    created_time = Column(Integer)
    updated_time = Column(Integer)

    @classmethod
    def new(cls, form):
        now = current_time()
        form.update({
            'updated_time': now,
            'created_time': now,
        })
        return cls(**form).save()

    @classmethod
    def find(cls, query):
        return cls.session.query(cls).filter_by(**query).all()

    @classmethod
    def find_one(cls, query):
        return cls.session.query(cls).filter_by(**query).first()

    @classmethod
    def update(cls, mappings):
        cls.session.bulk_update_mappings(cls, mappings)
        cls.session.commit()

    def save(self):
        self.session.add(self)
        self.session.commit()
        return self

    def delete(self):
        self.session.delete(self)
        self.session.commit()

    def json(self):
         m = deepcopy(self.__dict__)
         m.pop('_sa_instance_state', None)
         return m

class DataBase(object):

    Base = declarative_base()

    def __init__(self, uri):
        self.engine = create_engine(uri, echo=True)
        self.Model = self.Base
        self.session = sessionmaker(bind=self.engine)()
        meta = {
            'session': self.session,
        }
        meta.update(ModelMixin.__dict__)
        self.ModelMixin = type('ModelMixin', (), meta)
        _include_sqlalchemy(self)

    def create_all(self):
        self.Base.metadata.create_all(self.engine)
