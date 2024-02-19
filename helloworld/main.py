from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root(args):
    foo = None
    return {"message": "Hello World"}



