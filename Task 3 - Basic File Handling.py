def read_file(filename):  # Reads and returns the content of the file
    try:
        with open(filename, "r") as file:
            data = file.read()
        return data
    except FileNotFoundError:
        print("Error: The file does not exist.")
    except PermissionError:
        print("Error: Permission denied to read the file.")
    except Exception as e:
        print("Unexpected error while reading file:", e)
    return None

def write_file(filename, data):  # Writes data back to the file
    try:
        with open(filename, "w") as file:
            file.write(data)
        print("File updated successfully!")
    except PermissionError:
        print("Error: Permission denied to write to the file.")
    except Exception as e:
        print("Unexpected error while writing file:", e)

def find_and_replace(data, old_word, new_word):  # Replaces old_word with new_word in data
    if old_word not in data:
        print(f"'{old_word}' not found in file.")
    return data.replace(old_word, new_word)

def main():
    filename = input("Enter the file name (with .txt extension): ")

    content = read_file(filename)
    if content is None:
        return  # Stop program if file reading failed

    print("\nCurrent File Content:\n")
    print(content)

    old_word = input("\nEnter the word to find: ")
    new_word = input("Enter the replacement word: ")

    modified_content = find_and_replace(content, old_word, new_word)

    write_file(filename, modified_content)

if __name__ == "__main__":
    main()

