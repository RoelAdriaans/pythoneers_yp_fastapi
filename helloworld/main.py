from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root(args):    
    return {"message": "Hello World"}
