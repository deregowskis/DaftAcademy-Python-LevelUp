from fastapi import FastAPI, Response, status, HTTPException
from typing import NoReturn, Optional
from pydantic import BaseModel
import sqlite3
import sys

app = FastAPI()

class Category(BaseModel):
    name: str


@app.on_event("startup")
async def startup():
    app.db_connection = sqlite3.connect("northwind.db")
    app.db_connection.text_factory = lambda b: b.decode(errors="ignore")


@app.on_event("shutdown")
async def shutdown():
    app.db_connection.close()


@app.get("/")
async def main():
    return {"sqlite3_library_version": sqlite3.version, "sqlite_version": sqlite3.sqlite_version}


@app.get("/categories")
async def categories():
    categories = app.db_connection.execute('''SELECT CategoryID AS id, CategoryName AS name
                                              FROM Categories
                                              ORDER BY id
                                              ''')
    return {"categories": [{"id": row[0], "name": row[1]} for row in categories]}


@app.get("/customers")
async def customers():
    customers = app.db_connection.execute('''Select CustomerID AS id, CompanyName AS name, COALESCE(Address,''), COALESCE(PostalCode,''), COALESCE(City,''), COALESCE(Country,'')
                                             FROM Customers
                                             ORDER BY id COLLATE NOCASE
                                             ''')
    return {"customers": [{"id": row[0], "name": row[1], "full_address": "{} {} {} {}".format(row[2], row[3], row[4], row[5])} for row in customers]}
