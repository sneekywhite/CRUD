from pydantic import BaseModel



class PersonBase(BaseModel):
   name: str



class showPerson(BaseModel):
   user_id: int
   name:str

   class Config:
      form_attributes = True

   


    