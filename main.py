from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello you"}


@app.post("/")
async def test():
    return "ok buddy"
