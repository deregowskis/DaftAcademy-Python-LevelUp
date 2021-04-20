from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello world!"}


@app.get("/method")
def getmethod(request: Request):
    return {"method": request.method}


