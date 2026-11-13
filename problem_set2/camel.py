def convert_to_camel(some_string):
    for i in some_string:
        if i == i.upper():
            if i == some_string[0]:
                i = f"{i.lower()}"
            else:
                i = f"_{i.lower()}"
        print(i, end="")
        

def main():
    user_word = input("CamelCase: ").strip()
    convert_to_camel(user_word)


if __name__ == "__main__":
    main()