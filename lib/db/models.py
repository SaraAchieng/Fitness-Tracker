# models.py


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///fitness_database.db')

Base = declarative_base()