import string


def main():
    plate = input("Plate: ").strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate_number: str):
    if not 2 <= len(plate_number) <= 6:
        return False
    if plate_number[-1].isalpha():
        return False

    is_upper = False
    is_lower = False
    is_num = False
    num = ""

    for i in range(len(plate_number)):
        if plate_number[i] in string.punctuation:
            return False
        elif plate_number[i].isupper():
            is_upper = True
        elif plate_number[i].islower():
            is_lower = True
        elif plate_number[i].isdigit():
            num += plate_number[i]
            if num[0] == "0":
                return False
            is_num = True
    sum_types = sum([is_upper, is_lower, is_num])

    if sum_types < 2:
        return False

    return True


if __name__ == "__main__":
    main()
