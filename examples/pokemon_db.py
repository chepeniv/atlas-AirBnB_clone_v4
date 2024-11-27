#!/usr/bin/python3

import cmd
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

username = 'root'
password = 'root'
database = 'pokemon_db'
db_url = "mysql+mysqldb://{}:{}@localhost/{}".format(
        username,
        password,
        database)

Base = declarative_base()

class Pokemon(Base):
    __tablename__ = 'pokemon'

    name = Column(String(255), primary_key=True)
    type1 = Column(String(255))
    type2 = Column(String(255))
    hp = Column(Integer)
    attack = Column(Integer)
    defense = Column(Integer)
    special_attack = Column(Integer)
    special_defense = Column(Integer)
    speed = Column(Integer)

    def __init__(self, name):
        self.name = name

class Caught(Base):
    __tablename__ = 'caught'

    id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    name = Column(String(255))
    number = Column(Integer)

    def __init__(self, pokemon):
        self.name = pokemon.name
        self.number = 1

    def catch_another(self):
        self.number += 1

    def release_one(self):
        self.number -= 1

def connect():
    db_engine = create_engine(db_url, pool_pre_ping=True)
    Base.metadata.create_all(db_engine)
    Session = sessionmaker(db_engine)
    return Session()

class PokemonCommand(cmd.Cmd):
    prompt = 'gottacatchemall! '

    def preloop(self):
        self.session = connect()
    
    def do_catch(self, arg):
        args = arg.split()
        print('{}'.format(args))

    def do_quit(self, argstring):
        quit()
    do_EOF = do_quit
    do_exit = do_quit

if __name__ == "__main__":
    PokemonCommand().cmdloop()
