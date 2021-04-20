from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello world!"}


@app.get("/method")
def getmethod(request: Request):
    if request.method == 'GET':
        return {"method": "GET"}


