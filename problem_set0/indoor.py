def lower(some_string):
    return some_string.lower()

def main():
    user_input = lower(input("Enter anything").strip())
    print(user_input)

if __name__ == "__main__":
    main()
