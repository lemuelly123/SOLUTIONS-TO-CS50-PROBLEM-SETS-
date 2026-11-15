AVAILABLE_FUEL = 100


def guage(user):
    if "/" not in user:
        raise ValueError(f"Invalid format --->expected [x/y] but got {user!r} instead")
    x, y = user.split("/")
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
    if x == 0:
        return f"E"
    elif x == y:
        return f"F"
    return f"{round((x / y) * AVAILABLE_FUEL)}%"


def main():
    try:
        fuel_guage = input("Fraction: ").strip().lower()
        print(guage(fuel_guage))
    except ValueError as v:
        print(v)

if __name__ == "__main__":
    main()
