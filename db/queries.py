# queries.py

CREATE_TABLE_registered = """
    CREATE TABLE IF NOT EXISTS registered (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fullname TEXT,
    age TEXT,
    gender TEXT, 
    email TEXT,
    photo TEXT
    )
"""

INSERT_registered_QUERY = """
    INSERT INTO registered (fullname, age, gender, email, photo)
    VALUES (?, ?, ?, ?, ?)
"""

CREATE_TABLE_store = """
    CREATE TABLE IF NOT EXISTS store (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    modelname TEXT,
    size TEXT,
    price TEXT, 
    photo TEXT,
    product_id TEXT
    )
"""



CREATE_TABLE_store_details = """
    CREATE TABLE IF NOT EXISTS store_details (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    category TEXT,
    product_id TEXT,
    info_product TEXT
    )
"""

INSERT_store_QUERY = """
    INSERT INTO store (modelname, size, price, photo, productid)
    VALUES (?, ?, ?, ?, ?)
"""


INSERT_store_details_QUERY = """
    INSERT INTO store_details (category, product_id, info_product)
    VALUES (?, ?, ?)
"""

CREATE_TABLE_collection_products = """
    CREATE TABLE IF NOT EXISTS collection_products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    productid TEXT,
    collection TEXT
    )
"""

INSERT_collection_QUERY = """
    INSERT INTO collection_products (productid, collection)
    VALUES (?, ?)
"""