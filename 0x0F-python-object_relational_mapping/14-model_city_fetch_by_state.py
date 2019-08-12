#!/usr/bin/python3
""" doc """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
from sys import argv


if __name__ == "__main__":
    if len(argv) == 4:
        url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            argv[1], argv[2], argv[3], pool_pre_ping=True)
        engine = create_engine(url)
        Session = sessionmaker(bind=engine)
        session = Session()
        query = session.query(State, City).join(City, State.id == City.state_id).\
                order_by(City.id)
        for state, city in query:
            print('{}: ({}) {}'.format(state.name, city.id, city.name))
