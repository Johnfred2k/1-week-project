from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, Float
from database import Base

class Houses(Base):
    __tablename__ = "houses"
    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date)
    price = Column(Float)
    bedrooms = Column(Integer)
    #bathrooms = Column(Float)
    #sqft_living = Column(Integer)
    #sqft_lot = Column(Integer)
    #floors = Column(Float)
    #waterfront = Column(Float)
    #view = Column(Float)
    #condition = Column(Integer)
    #grade = Column(Integer)
    #sqft_above = Column(Integer)
    #sqft_basement = Column(String)
    #yr_built = Column(Integer)
    #yr_renovated = Column(Float)
    #zipcode = Column(Integer)
    #lat = Column(Float)
    #long = Column(Float)
    #sqft_living15 = Column(Integer)
    #sqft_lot15 = Column(Integer)