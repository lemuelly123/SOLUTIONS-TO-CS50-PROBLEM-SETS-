def file_extension(file_name):
    valid_file_extensions = [
        "gif",
        "jpg",
        "jpeg",
        "pdf",
        "txt",
        "png",
        "pdf",
        "zip",
    ]
    _, file_ext = file_name.split(".")
    file_ext = file_ext.strip().lower()
    if file_ext in valid_file_extensions:
        if file_ext in ["gif", "jpeg", "jpg", "png"]:
            return f"image/{file_ext}"
        elif file_ext in ["pdf", "txt"]:
            return f"text/{file_ext}"
        elif file_ext in ["zip"]:
            return f"compressed file/{file_ext}"
    else:
        return f"Invalid file format {file_name}"

def main():
    file = input("File name: ")
    print(file_extension(file))

if __name__ == "__main__":
    main()