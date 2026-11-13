valid_operandi = ["*", "+", "-", "/"]

def convert_to_float(num):
    try:
        num = float(num)
    except ValueError:
        print(f"Expected number but got {num!r} instead")
    return num

def interpret(expression):
    num1, operandi, num2 = expression.split(" ")
    x = convert_to_float(num1)
    y = convert_to_float(num2)
    if operandi not in valid_operandi:
        raise ValueError(f"Invalid operandi expected {[valid_operandi]} but got {operandi!r}")
    else:
        if operandi == "+":
            return x + y
        elif operandi == "-":
            return x - y
        elif operandi == "*":
            return x * y
        else:
            return x / y