from lib.db import db

class Persons(db.Model):
    __tablename__ = "persons"

    person_id = db.Column(db.String(), primary_key=True)
    last_name = db.Column(db.String())
    first_name = db.Column(db.String())
    address = db.Column(db.String())
    city = db.Column(db.String())

    def __init__(self, person_id, last_name, first_name, address, city):
        self.person_id = person_id
        self.last_name = last_name
        self.first_name = first_name
        self.address = address,
        self.city = city
