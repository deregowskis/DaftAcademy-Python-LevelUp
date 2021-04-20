from fastapi import FastAPI
from fastapi import Request

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello world!"}


@app.get("/method")
def root(request: Request):
    return {"method": f"{request.method}"}

@app.put("/method")
def root(request: Request):
    return {"method": f"{request.method}"}

@app.post("/method",status_code=201)
def root(request: Request):
    return {"method": f"{request.method}"}

@app.delete("/method")
def root(request: Request):
    return {"method": f"{request.method}"}

@app.options("/method")
def root(request: Request):
    return {"method": f"{request.method}"}


