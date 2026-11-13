def valid_answer():
    return [
        "42",
        "forty-two",
        "forty two",
    ]


def main():
    answer = (
        input(
            "What is the Answer to the Great Question of Life, the Universe, and Everything? "
        )
        .strip()
        .lower()
    )
    if answer not in valid_answer():
        return "No"
    return "yes"

if __name__ == "__main__":
    print(main())