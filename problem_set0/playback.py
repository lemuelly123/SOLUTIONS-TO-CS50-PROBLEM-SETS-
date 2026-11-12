def replace_space(some_string:str):
    return some_string.replace(" ", "...")

def main():
    result = replace_space(input("Enter text ").strip())
    print(result)

if __name__ == "__main__":
    main()
