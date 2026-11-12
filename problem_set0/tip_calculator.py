def main():
    cost = dollar_to_float(input("What is the cost of your meal? "))
    percent_tip = percent_to_float(input("What percent tip do you want to give? "))
    tip = cost * percent_tip
    print(f"Thank you for ${tip} tip")


def dollar_to_float(dollar_amount):
    try:
        if "$" in dollar_amount:
            _, dollar = dollar_amount.split("$")
            try:
                dollar = float(dollar)
                return dollar
            except ValueError:
                raise ValueError("Enter numbers only")  
        else:
            return float(dollar_amount)
    except ValueError:
        raise ValueError("Invalid format for dollar amount")

def percent_to_float(percentage):
    try:
        percentage = float(percentage)
        return float(percentage / 100)
    except ValueError:
        raise ValueError(f"Expected number for percentage got {percentage!r} instead")
if __name__ == "__main__":
    main()