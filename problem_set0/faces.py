def convert(some_string):
    if ":)" in  some_string:
        new = string = some_string.replace("):", "😊")
    elif ":(" in some_string:
        new_string  = some_string.replace(":(", "☹️")
    return new_string

def main():
    result = convert(input("Enter text "))
    print(result)

if __name__ == "__main__":
    main()