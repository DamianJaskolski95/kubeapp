from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import random
from database import crud, models, schemas
from database.database import SessionLocal, engine, Base

from pydantic import BaseModel

app = FastAPI()
random.seed()
val = random.randint(0, 1000)

def create_tables():
	print("create_tables")
	Base.metadata.create_all(bind=engine)

class Test():
    name: str
    name2: str
    value: int

    def __init__(self, name):
        self.name = name
        self.name2 = name + "2"
        self.value = random.randint(0, 1000)

test_list = []

@app.get("/")
def read_root():
    return {"Hello": val}

@app.get("/test/{test_name}")
def read_test(test_name: str):
    for t in test_list:
        if test_name == t.name:
            return {"obj": t, "n": t.name, "z": t.name2} 
    return {"is_in": "false"}

@app.put("/test/{test_name}")
def update_test(test_name: str):
    test_list.append(Test(test_name))
    return {"test_name": test_name, "status": "added","is_in": "true"}    

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/users/{user_id}/items/", response_model=schemas.Item)
def create_item_for_user(
    user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
):
    return crud.create_user_item(db=db, item=item, user_id=user_id)


@app.get("/items/", response_model=list[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items
