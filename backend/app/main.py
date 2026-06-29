from fastapi import FastAPI

app = FastAPI(
    title="MediVision AI API",
    description="AI-powered X-ray fracture detection backend",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to MediVision AI Backend!",
        "status": "Running Successfully"
    }