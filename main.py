from fastapi import FastAPI
import sqlite3
import sys

app = FastAPI()

@app.on_event("startup")
async def startup():
    app.db_connection = sqlite3.connect("northwind.db")
    app.db_connection.text_factory = lambda b: b.decode(errors="ignore")  # northwind specific 


@app.on_event("shutdown")
async def shutdown():
    app.db_connection.close()


@app.get("/")
async def main():
    return {"sqlite3_library_version": sqlite3.version, "sqlite_version": sqlite3.sqlite_version}


@app.get("/categories")
async def categories():
    categories = app.db_connection.execute('''select CategoryID as id, CategoryName as name from Categories order by id''').fetchall()
    return {"categories": [{"id": record[0], "name": record[1]} for record in categories]}


@app.get("/customers")
async def customers():
    customers = app.db_connection.execute('''select CustomerID as id, CompanyName as name, coalesce(Address,""), coalesce(PostalCode,""), coalesce(City,""), coalesce(Country,"") from Customers order by id collate nocase''').fetchall()
    return {"customers": [{"id": record[0], "name": record[1], "address": record[2], "postalcode": record[3],
                            "city": record[4], "country": record[5]} for row in customers]}
