def einstein_formula(mass):
    return mass * (3 **2)

def main():
    user_input = input("Enter mass ")
    try:
        int(user_input)
    except ValueError:
        print(f"Expected number for mass instead got {user_input!r}")
    result = einstein_formula(user_input)
    print(result)

if __name__ == "__main__":
    main()