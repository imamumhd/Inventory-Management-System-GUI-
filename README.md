Simple Inventory Management System

A basic command-line application for managing product inventory using Python and SQLite.

Features
* View Inventory: Display a list of all items, their quantities, and prices.
* Add Item: Insert a new item into the inventory with a name, quantity, and price.
* Update Item Quantity: Modify the stock quantity for an existing item by its ID.
* Delete Item: Remove an item from the inventory by its ID.
* SQLite Database: Stores inventory data persistently in a local `inventory.db` file.

Requirements
* Python 3.x
* The built-in `sqlite3` module (which is included with standard Python installations).

Project Structure
* `main.py`: Contains the main application loop and user interface logic. It imports functions from `inventory_functions.py`.
* `inventory_functions.py`: Contains the core logic for database interaction, including functions for connecting, adding, updating, deleting, and viewing items using the `sqlite3` library.
* `inventory.db`: The SQLite database file where all inventory data is persistently stored.

Workflow
1.  **View Inventory (Option 1):**
    ```
    Enter choice: 1

    Current Inventory:
    ID | Name | Quantity | Price
    ------------------------------
    # Existing items will be listed here
    ```
2.  **Add Item (Option 2):**
    ```
    Enter choice: 2
    Item name: Laptop
    Quantity: 5
    Price: 1250.00
    ```
3.  Update Item Quantity (Option 3):
    *First, view the inventory to get the item ID.*
    * *If 'Laptop' has ID 1:*
    ```
    Enter choice: 3
    Item ID to update: 1
    New quantity: 3
    ```
4.  Exit (Option 5):
    ```
    Enter choice: 5
    # The application closes and saves the changes.
    ```
    
