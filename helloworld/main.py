from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root(args):    
    return {"message": "Hello World"}

@app.get("/about")
async def about(args):    
    return {"message": "About the project"}  
