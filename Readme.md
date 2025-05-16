# 🏷️ DocumentTagger

DocumentTagger is a FastAPI-based application that detects and extracts text from uploaded documents (PDF, DOCX) and automatically generates relevant tags using Natural Language Processing (NLP).

## Features

-  Upload documents (PDF or DOCX)
-  Extract raw text from uploaded documents
-  Generate intelligent tags using KeyBERT
-  FastAPI backend with interactive Swagger docs
-  Docker support for containerized deployment

---

## Tech Stack

- **Backend**: FastAPI
- **Tag Generation**: `KeyBERT` + `sentence-transformers`
- **Containerization**: Docker

---
##  Setup Instructions

### 1. Clone the Repository

```
    git clone https://github.com/yourusername/DocumentTagger.git
    cd DocumentTagger
```

### 2. Create and Activate Virtual Environment

```
    python3 -m venv venv
    source venv/bin/activate
```

### 3. Install Dependencies 

```
    pip install -r requirements.txt
```

### 4. Run the FastAPI Server
```
uvicorn app.main:app --reload
```

Open your browser and go to: http://127.0.0.1:8000/docs to interact with the Swagger UI.


##  Docker Instructions

### 1. Build Docker Image

```
docker build -t documenttagger .
```

### 2. Run Container

```
docker run -d -p 8000:8000 documenttagger
```

Now visit http://localhost:8000/docs




