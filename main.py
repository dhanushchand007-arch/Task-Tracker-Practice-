from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from enum import Enum
from datetime import timezone,datetime
from fastapi.middleware.cors import CORSMiddleware
app=FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows local frontend html file to connect
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
task_id_counter = 1
class statusdata(str,Enum):
    TODO="todo"
    IN_PROGRESS = "in-progress"
    DONE="done"
class user_sent_data(BaseModel):
    description:str
    status:statusdata
class backenddata(user_sent_data):
    id:int
    createdAt:datetime
    updatedAt:datetime
db={}
@app.post("/tasks")
def senddata(data:user_sent_data):
    global task_id_counter
    current_id=task_id_counter
    now=datetime.now(timezone.utc)
    new_task=backenddata(
        id=task_id_counter,
        description=data.description,
        status=data.status,
        createdAt=now,
        updatedAt=now,
    )
    db[current_id]=new_task
    task_id_counter+=1
    return {"status":"sent!"}
@app.get("/tasks/data")
def getdata():
    return db
@app.delete("/tasks/delete/{a}")
def dltdata(a:int):
    if a not in db.keys():
        raise HTTPException(
            status_code=404,detail=f"id {a} not found"
        )
    db.pop(a)
    return {"new list":db}
@app.put("/tasks/{task_id}")
def updata(task_id:int,data:user_sent_data):
    if task_id not in db.keys():
        raise HTTPException(
            status_code=404,detail=f"id {task_id} not in the list"
        )
    now=datetime.now(timezone.utc)
    original=db[task_id].createdAt
    db[task_id]=backenddata(
        id=task_id,
        description=data.description,
        status=data.status,
        createdAt=original,
        updatedAt=now,
        )
    return {"updated":db}