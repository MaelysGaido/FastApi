from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Je vais faire pipi"}

@app.post("/")
async def test():
    return "ok buddy"