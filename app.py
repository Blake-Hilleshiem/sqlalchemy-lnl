from flask import Flask
from sqlalchemy import text, inspect
from uuid import uuid4

from config import database_name
from lib.db import db, init_db
from lib.sqlalchemy_session import create_db, add_one
from models.persons import Persons
from controllers.bulk_add_persons import bulk_add_persons

# === flask-sqlalchemy ===
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgres://127.0.0.1:5432/{database_name}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
init_db(app, db)

with app.app_context():
    db.create_all()
    bulk_add_persons()

# === from sqlalchemy ====
# create_db()
# add_one()