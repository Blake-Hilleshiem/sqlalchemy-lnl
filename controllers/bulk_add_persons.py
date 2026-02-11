from sqlalchemy import insert
from uuid import uuid4

from lib.db import db
from models.persons import Persons


def bulk_add_persons():
    # persons_list = []
    for i in range(0,100000):
        person = Persons(str(uuid4()),'ham', 'joe','123 St', 'Orem')
        db.session.add(person)

    #     persons_list.append({'person_id':str(uuid4()), 'last_name':'ham','first_name':"joe","address":"123 st", 'city':"Orem"})
    # db.session.execute(insert(Persons), persons_list)

    print('start commit')
    db.session.commit()
    print('finished commit')