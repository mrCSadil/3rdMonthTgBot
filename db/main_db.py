# main_db.py
import sqlite3
from db import queries


# db = sqlite3.connect('db/registered.sqlite3')
db = sqlite3.connect('db/store.sqlite3')
cursor = db.cursor()


async def DataBase_create():
    if db:
        print('База данных подключена!')
    cursor.execute(queries.CREATE_TABLE_collection_products)
    cursor.execute(queries.CREATE_TABLE_registered)
    cursor.execute(queries.CREATE_TABLE_store)
    cursor.execute(queries.CREATE_TABLE_store_details)


async def sql_insert_registered(fullname, age, gender, email, photo):
    cursor.execute(queries.INSERT_registered_QUERY, (
        fullname, age, gender, email, photo
    ))
    db.commit()

async def sql_insert_store(modelname, size, price, product_id, photo):
    cursor.execute(queries.INSERT_store_QUERY, (
        modelname, size, price, product_id, photo
    ))
    db.commit()

async def sql_insert_collections(product_id, collection):
    cursor.execute(queries.INSERT_collection_QUERY, (
        product_id, collection
    ))
    db.commit()

async def sql_insert_store_detail(category, product_id, info_product):
    cursor.execute(queries.INSERT_store_details_QUERY, (
        category, product_id, info_product
    ))
    db.commit()





# CRUD - Read
# =====================================================

# Основное подключение к базе (Для CRUD)
def get_db_connection():
    conn = sqlite3.connect('db/store.sqlite3')
    conn.row_factory = sqlite3.Row
    return conn


def fetch_all_products():
    conn = get_db_connection()
    products = conn.execute("""
    SELECT s.*, sd.*, c.*
    FROM store s
    INNER JOIN store_details sd ON s.productid = sd.product_id
    INNER JOIN collection_products c ON s.productid = c.productid
    """).fetchall()
    conn.close()
    return products

# CRUD - Delete
# =====================================================

def delete_product(product_id):
    conn = get_db_connection()

    conn.execute('DELETE FROM store WHERE productid = ?', (product_id,))

    conn.commit()
    conn.close()