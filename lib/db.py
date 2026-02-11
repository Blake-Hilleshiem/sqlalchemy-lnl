from flask import Flask
from flask_sqlalchemy import SQLAlchemy

__all__ = ('db', 'init_db')

# our global DB ojbect (imported by models and views)
db = SQLAlchemy()
metadata = db.Model.metadata

# support importing a functioning session query
query = db.session.query


def init_db(app=None, db=None):
    """Initializes the global database object used by the app."""
    if isinstance(app, Flask) and isinstance(db, SQLAlchemy):
        db.init_app(app)
    else:
        raise ValueError('Cannot Initialize Database Without db and app Objects.')