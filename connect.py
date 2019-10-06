from sqlalchemy import Column, Integer, String, create_engine, or_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from math import floor

import cx_Oracle

hostname = 'localhost'
port = 1521
dbName = 'xe'

user = 'tripartio'  # tripartio << должен вводиться пользователем
password = 'q1w2r3t4'  # q1w2r3t4 << должен вводиться пользователем

sid = cx_Oracle.makedsn(hostname, port, sid=dbName)

connect_str = 'oracle+cx_oracle://{user}:{password}@{sid}'.format(user=user,
                                                                  password=password,
                                                                  sid=sid)
engine = create_engine(connect_str, echo=False)
Base = declarative_base(engine)


class DescWrk(Base):
    __tablename__ = 'DESC_WRK'
    __table_args__ = {'autoload': True}


class Plan(Base):
    __tablename__ = 'PLAN'
    __table_args__ = {'autoload': True}


class Projs(Base):
    __tablename__ = 'PROJS'
    __table_args__ = {'autoload': True}


class RefBookW(Base):
    __tablename__ = 'RB_WRK'
    __table_args__ = {'autoload': True}


class Unit(Base):
    __tablename__ = 'UNIT'
    __table_args__ = {'autoload': True}


def loadSession():
    metadata = Base.metadata
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

if __name__ == '__main__':
    session = loadSession()