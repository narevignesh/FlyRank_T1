from fastapi import FastAPI, HTTPException, Response
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI(title="FlyRank Task Manager API")

class TaskCreate(BaseModel):
    title: Optional[str] = None

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    done: Optional[bool] = None

class Task(BaseModel):
    id: int
    title: str
    done: bool = False

# In-memory database pre-filled with 3 tasks
tasks_db: List[Task] = [
    Task(id=1, title="Buy groceries", done=False),
    Task(id=2, title="Finish homework", done=True),
    Task(id=3, title="Call friend", done=False),
]

@app.get("/")
def read_root():
    """Get basic API metadata and description."""
    return {
        "name": "Task API",
        "version": "1.0",
        "endpoints": ["/tasks"]
    }

@app.get("/health")
def read_health():
    """Get server health status."""
    return {
        "status": "ok"
    }

@app.get("/tasks", response_model=List[Task])
def read_tasks():
    """Retrieve the complete list of tasks."""
    return tasks_db

@app.get("/tasks/{task_id}", response_model=Task)
def read_task(task_id: int):
    """Retrieve details of a single task by ID."""
    for task in tasks_db:
        if task.id == task_id:
            return task
    return JSONResponse(status_code=404, content={"error": f"Task {task_id} not found"})

@app.post("/tasks", response_model=Task, status_code=201)
def create_task(task_data: TaskCreate):
    """Create a new task with validation."""
    if not task_data.title or task_data.title.strip() == "":
        return JSONResponse(status_code=400, content={"error": "Title is required and cannot be empty"})
    
    next_id = max([t.id for t in tasks_db]) + 1 if tasks_db else 1
    new_task = Task(id=next_id, title=task_data.title, done=False)
    tasks_db.append(new_task)
    return new_task

@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task_data: TaskUpdate):
    """Update an existing task's title and/or done status."""
    if task_data.title is None and task_data.done is None:
        return JSONResponse(status_code=400, content={"error": "Body cannot be empty"})
    
    if task_data.title is not None and task_data.title.strip() == "":
        return JSONResponse(status_code=400, content={"error": "Title cannot be empty"})

    for task in tasks_db:
        if task.id == task_id:
            if task_data.title is not None:
                task.title = task_data.title
            if task_data.done is not None:
                task.done = task_data.done
            return task
    
    return JSONResponse(status_code=404, content={"error": f"Task {task_id} not found"})

@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    """Remove a task from the list by ID."""
    for index, task in enumerate(tasks_db):
        if task.id == task_id:
            tasks_db.pop(index)
            return Response(status_code=204)
    return JSONResponse(status_code=404, content={"error": f"Task {task_id} not found"})
