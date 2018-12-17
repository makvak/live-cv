from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

# TODO put config db
engine = create_engine('sqlite:///cv_lib.db')

Base = declarative_base()
