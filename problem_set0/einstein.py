def einstein_formula(mass):
    return mass * 300000000 ** 2

def main():
    user_input = input("Enter mass: ")
    try:
        user_input = int(user_input)
    except ValueError:
        print(f"Expected number for mass instead got {user_input!r}")
    result = einstein_formula(user_input)
    print(f"{result}J")

if __name__ == "__main__":
    main()