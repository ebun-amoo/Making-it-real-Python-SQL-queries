# Product Interface
import sqlite3
DATABASE_FILE = 'products.db'

db = sqlite3.connect(DATABASE_FILE)
#making the tuple accessible
db.row_factory = sqlite3.Row
#retrieving data from products table
# cursor = db.execute('SELECT * FROM products')
# #fetching the data from the cursor
#cursor.fetchall()


def select_all_products():
    cursor = db.execute('SELECT * FROM products;')
    return cursor.fetchall()

def select_product_by_id(_id):
    cursor = db.execute("SELECT * FROM products WHERE id = ?;", [_id])
    return cursor.fetchone()

def products_cheaper_than(price):
    cursor = db.execute("SELECT * FROM products WHERE price < ?;", [price])
    return cursor.fetchall()

def get_last_product():
    cursor = db.execute("SELECT * FROM products ORDER BY id DESC LIMIT 1;")
    return cursor.fetchone()

def add_product(name, price, quantity):
    db.execute("INSERT INTO products(name, price, quantity) VALUES(?, ?, ?);", [name, price, quantity])
    db.commit()
    last_product = get_last_product()
    return last_product

def product_details(product):
    return f"{product['name']}: ${product['price']}. {product['quantity']} left in stock"

def product_overview(product):
    return f"{product['id']}    {product['name']}"
