import psycopg2
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

connection = psycopg2.connect(user="user", password="password")
cursor = connection.cursor()

connection.autocommit = True
create_database_sql = "CREATE DATABASE fastapi_films"

try:
    cursor.execute(create_database_sql)
except psycopg2.errors.DuplicateDatabase:
    pass

cursor.close()
connection.close()


engine = create_engine("postgresql+psycopg2://user:password@localhost/fastapi_films")
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class Films(Base):
    __tablename__ = "films"
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    genre = Column(String(50), nullable=False)
    year = Column(Integer(), nullable=False)
    director = Column(String(50), nullable=False)


Base.metadata.create_all(engine)
