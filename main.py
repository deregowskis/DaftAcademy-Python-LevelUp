from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    response.status_code=200
    return {"message": "Hello world!"}


@app.get("/method")
def getmethod():
    if request.method == 'GET':
        response.status_code=200
        return {"method": "GET"}
