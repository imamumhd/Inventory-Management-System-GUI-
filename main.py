from inventory_functions import connect_db, add_item, update_item, delete_item, view_inventory
def main():
    conn = connect_db()
    while True:
        print("\nInventory Menu:")
        print("1. View Inventory")
        print("2. Add Item")
        print("3. Update Item Quantity")
        print("4. Delete Item")
        print("5. Exit")

        choice = input("Enter choice: ")
        if choice == "1":
            view_inventory(conn)
        elif choice == "2":
            name = input("Item name: ")
            quantity = int(input("Quantity: "))
            price = float(input("Price: "))
            add_item(conn, name, quantity, price)
        elif choice == "3":
            item_id = int(input("Item ID to update: "))
            quantity = int(input("New quantity: "))
            update_item(conn, item_id, quantity)
        elif choice == "4":
            item_id = int(input("Item ID to delete: "))
            delete_item(conn, item_id)
        elif choice == "5":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
