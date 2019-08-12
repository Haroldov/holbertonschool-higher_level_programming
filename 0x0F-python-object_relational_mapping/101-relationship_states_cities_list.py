#!/usr/bin/python3
""" doc """
from sqlalchemy import create_engine, desc
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
from sys import argv


if __name__ == "__main__":
    if len(argv) == 4:
        url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            argv[1], argv[2], argv[3], pool_pre_ping=True)
        engine = create_engine(url)
        Base.metadata.create_all(engine)
        session = sessionmaker(bind=engine)()
        query = session.query(State)
        for ins in query:
            print("{}: {}".format(ins.id, ins.name))
            for ins2 in ins.cities:
                print("\t{}: {}".format(ins2.id, ins2.name))
