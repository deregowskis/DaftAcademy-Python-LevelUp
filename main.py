from fastapi import FastAPI, HTTPException
import sqlite3
import sys

app = FastAPI()



@app.on_event("startup")
async def startup():
    app.db_connection = sqlite3.connect("northwind.db")
    app.db_connection.text_factory = lambda b: b.decode(errors="ignore")


@app.on_event("shutdown")
async def shutdown():
    app.db_connection.close()


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

@app.get("/products/{id}")
async def products(id: int):
    product = app.db_connection.execute('''SELECT ProductID, ProductName
                                           FROM Products
                                           WHERE ProductID = :id
                                           ''', {'id': id}).fetchone()
    if product is None:
        raise HTTPException(status_code=404)
    return {"id": product[0], "name": product[1]}