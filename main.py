from fastapi import FastAPI
from fastapi import Request

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello world!"}


@app.get("/method")
def root(request: Request):
    return {"method": f"{request.method}"}


