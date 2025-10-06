import sqlite3

# Connect to the database and create the items table if it doesn't exist
def connect_db():
    conn = sqlite3.connect("inventory.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS items (
            item_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            price REAL NOT NULL
        )
    """)
    conn.commit()
    return conn

# Add a new item to the inventory
def add_item(conn, name, quantity, price):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO items (name, quantity, price) VALUES (?, ?, ?)", (name, quantity, price))
    conn.commit()

# Update the quantity of an existing item
def update_item(conn, item_id, quantity):
    cursor = conn.cursor()
    cursor.execute("UPDATE items SET quantity = ? WHERE item_id = ?", (quantity, item_id))
    conn.commit()

# Delete an item from the inventory
def delete_item(conn, item_id):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM items WHERE item_id = ?", (item_id,))
    conn.commit()

# View all items in the inventory
def view_inventory(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM items")
    items = cursor.fetchall()
    print("\nCurrent Inventory:")
    print("ID | Name | Quantity | Price")
    print("-" * 30)
    for item in items:
        print(f"{item[0]} | {item[1]} | {item[2]} | ₦{item[3]:,.2f}")
