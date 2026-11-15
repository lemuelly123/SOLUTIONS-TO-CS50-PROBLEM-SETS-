menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    price_of_items = 0
    items_ordered = []
    try:
        while True:
            user_order = input("Item: ").strip().title()
            if user_order not in menu:
                print("Item not available")
                continue
            items_ordered.append(user_order)
            price_of_items += menu[user_order]
            print(f"Total: ${price_of_items}")
    except EOFError:
        if items_ordered:
            print("Enjoy your meal")
        else:
            print("No order")

if __name__ == "__main__":
    main()