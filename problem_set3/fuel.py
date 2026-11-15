AVAILABLE_FUEL = 100

def guage(fraction):
    ...

def check_x_y(x, y):
    try:
        x = int(x)
    except ValueError:
        return f"Expected integer but got {x!r}: {type(x)} instead"
    try:
        y = int(y)
    except ValueError:
        return f"Expected integer but got {x!r}: {type(y)} instead"
    if x < 0 or y <= 0 or x > y:
        raise ValueError("Invalid parameter provided")
    return (x / y) * AVAILABLE_FUEL

def main():
    ...

if __name__ == "__main__":
    main()
