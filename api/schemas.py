from typing import Optional
from pydantic import BaseModel
from datetime import date

class HouseModel(BaseModel):
    id: int
    date: date
    price: float
    bedrooms: int
    #bathrooms: float
    #sqft_living: int
    #sqft_lot: int
    #floors: float
    #waterfront: float
    #view: float
    #condition: int
    #grade: int
    #sqft_above: int
    #sqft_basement: str
    #yr_built: int
    #yr_renovated: float
    #zipcode: int
    #lat: float
    #long: float
    #sqft_living15: int
    #sqft_lot15: int

    class Config:
        orm_mode = True

class HouseOut(BaseModel):
    id: int
    date: date
    price: float
    bedrooms: int
    #bathrooms: float
    #sqft_living: int
    #sqft_lot: int
    #floors: float
    #waterfront: float
    #view: float
    #condition: int
    #grade: int
    #sqft_above: int
    #sqft_basement: str
    #yr_built: int
    #yr_renovated: float
    #zipcode: int
    #lat: float
    #long: float
    #sqft_living15: int
    #sqft_lot15: int

    class Config:
        orm_mode = True

class HouseUpdate(BaseModel):
    id: int
    date: date
    price: float
    bedrooms: int
    #bathrooms: float
    #sqft_living: int
    #sqft_lot: int
    #floors: float
    #waterfront: float
    #view: float
    #condition: int
    #grade: int
    #sqft_above: int
    #sqft_basement: str
    #yr_built: int
    #yr_renovated: float
    #zipcode: int
    #lat: float
    #long: float
    #sqft_living15: int
    #sqft_lot15: int

    class Config:
        orm_mode = True