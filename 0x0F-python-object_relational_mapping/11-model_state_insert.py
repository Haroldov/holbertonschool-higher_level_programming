#!/usr/bin/python3
""" doc """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv


if __name__ == "__main__":
    if len(argv) == 4:
        url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            argv[1], argv[2], argv[3], pool_pre_ping=True)
        engine = create_engine(url)
        Session = sessionmaker(bind=engine)
        session = Session()
        new_state = State(name='Louisiana')
        session.add(new_state)
        session.commit()
        query = session.query(State).filter(State.name == 'Louisiana')
        for ins in query:
            print("{}".format(ins.id))
