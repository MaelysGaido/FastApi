from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello yall"}

@app.post("/")
async def test():

     return "ok buddy"