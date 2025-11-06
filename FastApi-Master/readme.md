# FastAPI CRUD Starter
A simple and clean **FastAPI** starter project to help you build RESTful APIs quickly using **Python 3.10+**.
---

## Features

* FastAPI framework
* Auto-generated Swagger and ReDoc docs
* Hot reload using Uvicorn
* Structured project setup

---

## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/fastapi_crud.git
cd fastapi_crud
```

### 2. Create and Activate Virtual Environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Application

### 1. Start FastAPI Server

```bash
uvicorn main:app --reload
```

### 2. Open in Browser

* API Root → [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
* Swagger Docs → [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* ReDoc Docs → [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## Example Endpoint

**main.py**

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}
```

---

## 📦 Dependencies

* fastapi
* uvicorn

Install them using:

```bash
pip install fastapi uvicorn
```
