CREATE_TABLE_store = """
    CREATE TABLE IF NOT EXISTS store (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    modelname TEXT,
    size TEXT,
    price TEXT, 
    productid TEXT,
    photo TEXT
    )
"""

INSERT_store_QUERY = """
    INSERT INTO store (modelname, size, price, productid, photo)
    VALUES (?, ?, ?, ?, ?)
"""


CREATE_TABLE_products_details  = """
    CREATE TABLE IF NOT EXISTS products_details (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    productid TEXT,
    category TEXT,
    infoproduct TEXT
    )
"""

INSERT_products_details_QUERY = """
    INSERT INTO products_details (productid, category, infoproduct)
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
    INSERT INTO collection (id, productid, collcetion)
    VALUES (?, ?)
"""