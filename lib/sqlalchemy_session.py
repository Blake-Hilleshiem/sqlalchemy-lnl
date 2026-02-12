
# === Core ===
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, insert
from config import database_name

engine = create_engine(f"postgres://127.0.0.1/{database_name}")
connection = engine.connect()

metadata = MetaData()

contacts = Table('contacts', metadata, Column('contact_id', Integer, primary_key=True), Column("name", String))

def create_db():
    metadata.create_all(engine)

def add_one():
    stmt = contacts.insert().values(contact_id=3, name='Bro')
    connection.execute(stmt)




#  === ORM (SQLAlchemy v2)===
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, declarative_base
# from config import database_name

# engine = create_engine(f"postgres://127.0.0.1/{database_name}")
# Base = declarative_base()

# Base.metadata.create_all(engine)
# Session = sessionmaker(bind=engine)
# session = Session()

# new_person = Contacts(1, 'Blake')
# session.add(new_person)
# session.commit()
