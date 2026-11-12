def main():
    ...


def dollar_to_float(dollar_amount):
    if "$" in dollar_amount:
        _, dollar = dollar_amount.split("$")
        try:
            dollar = float(dollar)
            return dollar
        except ValueError:
            print("Enter numbers only")  
    else:
        return float(dollar_amount)


def percent_to_float(percentage):
    return float(percentage) / 100

dollar_to_float("100")
