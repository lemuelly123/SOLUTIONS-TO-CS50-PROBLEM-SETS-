def greeting(greet):
    greet = greet.strip().lower()
    if greet.strip().lower() == 'hello':
        return "$0"
    elif "h" in greet:
        return "$20"
    else:
        return "$100"

def main():
    user_greet = input("Greeting: ")
    print(greeting(user_greet))

if __name__ == "__main__":
    main()