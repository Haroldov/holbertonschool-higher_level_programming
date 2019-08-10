#!/usr/bin/python3
# doc
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
        for ins in session.query(State).order_by(State.id):
            print("{}: {}".format(ins.id, ins.name))
