def main():
    try:
        grocery_items = {}
        while True:
            items = input("").strip()
            if items in grocery_items:
                grocery_items[items] += 1
                continue
            grocery_items[items] = 1
    except EOFError:
        for items, num in sorted(grocery_items.items()):
            print(f"{num} {items.upper()}")


if __name__ == "__main__":
    main()
