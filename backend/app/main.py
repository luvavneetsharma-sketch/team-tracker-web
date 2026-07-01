from fastapi import FastAPI

app = FastAPI(
    title="Team Tracker API",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "Team Tracker API is running"
    }

@app.get("/health")
def health():
    return {
        "status": "ok"
    }