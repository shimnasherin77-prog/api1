# Create a FastAPI app that allows users to:
# ⿡ Add a "task" to a temporary list using POST
# ⿢ Retrieve all tasks using GET
#
# Details:
# - Each task should have:
#     - "title" (string)
#     - "completed" (boolean)
# - Store tasks in a simple Python list (temporary storage)
#
# Endpoints to create:
# 1. POST /addtask
#    - Accepts JSON body:
#        {
#            "title": "Buy groceries",
#            "completed": false
#        }
#    - Adds the task to the list
#    - Returns a success message with the task title
#
# 2. GET /gettasks
#    - Returns all tasks currently in the list
#    - Example response:
#        {
#            "tasks": [
#                {"title": "Buy groceries", "completed": false},
#                {"title": "Walk the dog", "completed": true}
#            ]
#        }
from fastapi import FastAPI,Request

app = FastAPI()

tasks = []

@app.post("/addtask")
async def add_task(request:Request):

    data = await request.json()

    title = data.get("title")
    completed = data.get("completed")

    task = {"title":title,"completed":completed}
    tasks.append(task)

    return {"message":f"{title},{completed}successfully added"}

@app.get("/gettasks")

def get_tasks():
  return{"tasks":tasks}