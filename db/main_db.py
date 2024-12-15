import sqlite3
from db import queries

store_db = sqlite3.connect('db/store.sqlite3')
products_db = sqlite3.connect('db/products_details.sqlite3')

store_cursor = store_db.cursor()
products_cursor = products_db.cursor()

async def database_create_store():
    if store_db:
        print('Store database already exists')
    store_cursor.execute(queries.CREATE_TABLE_store)

async def database_create_products_details():
    if products_db:
        print('Products details database already exists')
    products_cursor.execute(queries.CREATE_TABLE_products_details)

async def sql_insert_store(modelname, size, price, productid, photo):
    store_cursor.execute(queries.INSERT_store_QUERY, (
        modelname, size, price, productid, photo
    ))
    store_db.commit()

async def sql_insert_products_details(productid, category, infoproduct):
    products_cursor.execute(queries.INSERT_products_details_QUERY, (
        productid, category, infoproduct
    ))
    products_db.commit()