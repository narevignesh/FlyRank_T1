# FlyRank Task Manager API

A simple, in-memory to-do list CRUD API built with Python and FastAPI. This project was developed step-by-step through six progressive development stages.

## 🚀 Getting Started

To install and run the API locally in under 5 minutes:

### 1. Install Dependencies
Make sure you have Python 3.10+ installed, then run:
```bash
pip install -r requirements.txt
```

### 2. Start the API Server
Run the Uvicorn development server:
```bash
uvicorn main:app --reload --port 8000
```

The server will start at `http://127.0.0.1:8000`.

---

## 🗃️ API Endpoint Table

| HTTP Method | Path | Action | Description | Response Status |
| :--- | :--- | :--- | :--- | :--- |
| **GET** | `/` | Root | Describes the API metadata | `200 OK` |
| **GET** | `/health` | Health Check | Verifies if the server is running | `200 OK` |
| **GET** | `/tasks` | List Tasks | Retrieves all tasks in the list | `200 OK` |
| **GET** | `/tasks/{id}` | Read Task | Retrieves a single task by ID | `200 OK` / `404 Not Found` |
| **POST** | `/tasks` | Create Task | Creates a new task (Validates title) | `201 Created` / `400 Bad Request` |
| **PUT** | `/tasks/{id}` | Update Task | Replaces title/done status of a task | `200 OK` / `400 Bad Request` / `404 Not Found` |
| **DELETE** | `/tasks/{id}` | Delete Task | Deletes a task by ID | `204 No Content` / `404 Not Found` |

---

## 📋 Example Curl Output

### Create a Task (`POST /tasks`)
```bash
curl -i -X POST http://localhost:8000/tasks -H "Content-Type: application/json" -d '{"title":"Buy milk"}'
```

**Response:**
```http
HTTP/1.1 201 Created
date: Sat, 18 Jul 2026 17:02:11 GMT
server: uvicorn
content-length: 44
content-type: application/json

{"id":4,"title":"Buy milk","done":false}
```

### Get All Tasks (`GET /tasks`)
```bash
curl -i http://localhost:8000/tasks
```

**Response:**
```http
HTTP/1.1 200 OK
date: Sat, 18 Jul 2026 17:02:20 GMT
server: uvicorn
content-length: 243
content-type: application/json

[
  {"id":1,"title":"Buy groceries","done":false},
  {"id":2,"title":"Finish homework","done":true},
  {"id":3,"title":"Call friend","done":false},
  {"id":4,"title":"Buy milk","done":false}
]
```

### Get Non-existent Task (`GET /tasks/99`)
```bash
curl -i http://localhost:8000/tasks/99
```

**Response:**
```http
HTTP/1.1 404 Not Found
date: Sat, 18 Jul 2026 17:02:30 GMT
server: uvicorn
content-length: 30
content-type: application/json

{"error":"Task 99 not found"}
```

---

## 🔍 Swagger UI Documentation

FastAPI provides built-in interactive Swagger documentation. Start the server and navigate to:
👉 **[http://localhost:8000/docs](http://localhost:8000/docs)**

You can use the "Try it out" button directly on the web page to execute operations against all endpoints.


