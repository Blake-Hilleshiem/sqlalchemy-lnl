from flask import Flask
from sqlalchemy import text, inspect
from uuid import uuid4

from lib.db import db, init_db
from config import database_name
from models.persons import Persons
from controllers.bulk_add_persons import bulk_add_persons

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgres://127.0.0.1:5432/{database_name}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
init_db(app, db)

with app.app_context():
    # inspector = inspect(db.engine)
    # tables = inspector.get_table_names()
    db.create_all()
