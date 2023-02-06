# CLI Interface for products database

from products import *

def options():
    return ("""
    1. Show all products
    2. Show product details
    3. Add a product
    4. Search products by price
    5. Exit""")

def main():
    while True:
        print(options())
        choice = input()
        if choice == "1":
            show_all_products()
        elif choice == "2":
            show_product_details()
        elif choice == "3":
            show_add_product()
        elif choice == "4":
            search_by_price()
        elif choice == "5":
            exit()
        else:
            print("Enter an option from 1-5")
        print()
        input("Press enter to continue")

def show_all_products():
    print("--- Products ---")
    print("ID    Name")
    for product in select_all_products():
        print(product_overview(product))

def show_product_details():
    input_id = input("Enter product id to show: ")
    while not input_id.isnumeric():
        print("Id must be an integer.")
        input_quantity = input("Enter product id to show: ")
    show_id = int(input_id)

    product_to_show = select_product_by_id(show_id)
    if product_to_show:
        print(product_details(product_to_show))
    else:
        print("Product not found")

def show_add_product():
    # get name
    name = input("Enter product name: ")

    # get price
    input_price = input("Enter product price: ")
    price = None
    while not price:
        try:
            price = float(input_price)
        except:
            print("Price must be a number.")
            input_price = input("Enter product price: ")

    # get quantity
    input_quantity = input("Enter product quantity: ")
    while not input_quantity.isnumeric():
        print("Quantity must be an integer.")
        input_quantity = input("Enter product quantity: ")
    quantity = int(input_quantity)

    # add product
    added = add_product(name, price, quantity)
    print(f"Added {product_details(added)}")

def search_by_price():
    print("Show products below a certain price.")
    input_price = input("Enter maximum product price: ")
    price = None
    while price == None:
        try:
            price = float(input_price)
        except:
            print("Price must be a number.")
            input_price = input("Enter maximum product price: ")

    
    results = products_cheaper_than(price)
    if results:
        print(f"The products cheaper than {price} are:")
        for product in results:
            print(product_details(product))
    else:
        print(f"No products cheaper than {price}.")

if __name__ == "__main__":
    main()
