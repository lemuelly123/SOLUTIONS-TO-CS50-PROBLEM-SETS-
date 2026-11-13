valid_operandi = ["*", "+", "-", "/"]

def convert_to_float(num):
    try:
        num = float(num)
    except ValueError:
        print(f"Expected number but got {num!r} instead")
    return num

def interpret(expression):
    try:
        num1, operandi, num2 = expression.split(" ")
    except ValueError:
        return f"Invalid format for expression expected 'x [/,*,-,+] y' but got {expression}"
    x = convert_to_float(num1)
    y = convert_to_float(num2)
    if operandi not in valid_operandi:
        raise ValueError(f"Invalid operandi expected: {[valid_operandi]} but got {operandi!r}")
    else:
        if operandi == "+":
            return x + y
        elif operandi == "-":
            return x - y
        elif operandi == "*":
            return x * y
        else:
            return x / y

def main():
    user_expression = input("Enter expression: ")
    print(interpret(user_expression))

if __name__ == "__main__":
    main()