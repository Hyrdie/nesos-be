from pydantic import BaseModel
from typing import List

class Menu(BaseModel):
    name:str
    price:int

class TimeOpen(BaseModel):
    day_open:str
    status_open:bool
    start_time:str
    end_time:str

class Facility(BaseModel):
    name:str

class Payment(BaseModel):
    name:str

class Service(BaseModel):
    name:str


class DetailPartner(BaseModel):
    partner_name:str
    category_name:str
    email:str
    menu:List[Menu]
    time_open:List[TimeOpen]
    facility:List[Facility]
    payment:List[Payment]
    service:List[Service]
    