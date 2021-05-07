from sqlalchemy import (
    create_engine, Column, Integer, String, ForeignKey
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('sqlite:///test.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Campaign(Base):
    __tablename__ = 'campaign'

    id = Column(Integer, primary_key=True, autoincrement=True)
    campaign_name = Column(String(50))
    amount_contributed = Column(Integer, default=0)
    user_email = Column(String(50))


Base.metadata.create_all(engine)
