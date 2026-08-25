from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"message": "Helloo Worldd"}

@app.get("/health")
def health():
    return {"status": "healthy"}
