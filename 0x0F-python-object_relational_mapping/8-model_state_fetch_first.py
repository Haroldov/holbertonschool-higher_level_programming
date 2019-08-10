#!/usr/bin/python3
""" prints the first State object from the database hbtn_0e_6_usa """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv


if __name__ == "__main__":
    if len(argv) == 4:
        url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            argv[1], argv[2], argv[3])
        engine = create_engine(url)
        Session = sessionmaker(bind=engine)
        session = Session()
        query = session.query(State).filter(State.id == 1).all()
        if len(query) != 0:
            print("{}: {}".format(query[0].id, query[0].name))
        else:
            print("Nothing")
