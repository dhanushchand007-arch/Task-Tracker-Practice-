from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from enum import Enum
from datetime import timezone,datetime
app=FastAPI()
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
        id:task_id_counter,
        description=data.description,
        status=data.status,
        createdAt=now,
        updatedAt=now
    )
    db[current_id]=new_task
    task_id_counter+=1
@app.get("/tasks/data")
def getdata():
    return db
