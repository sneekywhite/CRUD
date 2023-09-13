from fastapi import FastAPI, HTTPException, Depends, status
from typing import Annotated
import models
from sqlalchemy.orm import Session
from database import sessionLocal, engine
from schemas import PersonBase, showPerson



app = FastAPI()

models.Base.metadata.create_all(engine)


def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.post("/api/", status_code=status.HTTP_201_CREATED, response_model= showPerson, tags=['person'])
async def create_person(request:PersonBase, db: db_dependency):
    person = models.Person(**request.model_dump())
    db.add(person)
    db.commit()
    db.refresh(person)
    return person


@app.delete('/api/{user_id}/', status_code=status.HTTP_204_NO_CONTENT, tags=['deletePerson'])
def deletePerson(user_id, db: db_dependency):
    person = db.query(models.Person).filter(models.Person.user_id==user_id).first()
    if not person:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"person with the id {user_id} is not available")
    
    db.delete(person)
    db.commit()
    


@app.put('/api/{user_id}/', status_code=status.HTTP_200_OK, tags=['updatePerson'])
def update_person(user_id, request:showPerson, db:db_dependency):
    db.query(models.Person).filter(models.Person.user_id == user_id).update({'name':request.name})
    db.commit()
    return 'updated successfully'
    



@app.get('/api/{user_id}/', status_code=status.HTTP_200_OK, response_model= showPerson, tags=['getPerson'])
async def get_person(user_id, db:db_dependency):
    person = db.query(models.Person).filter(models.Person.user_id==user_id).first()
    if not person:
        #response.status_code = status.HTTP_404_NOT_FOUND
        #return {'detail': f"Blog with the id {id} is not available"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"person with the id {user_id} is not available")
    
    return person



