def remove_vowel(some_string):
    result = ""
    for i in some_string:
        if i.lower() in ['a', 'e', 'i', 'o', 'u']:
            pass
        else:
            result += i
    return result

def main():
    twitter = remove_vowel(input("Enter word: "))
    print(twitter)


if __name__ == "__main__":
    main()