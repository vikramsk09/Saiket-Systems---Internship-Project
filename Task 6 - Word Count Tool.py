def word_counter(file):
    try:
        with open(file, "r") as f:
            count = 0
            for data in f:
                words = data.split()
                count += len(words)
            else:
                return count
    except FileNotFoundError:
        print("File not found!")
    return None

def line_counter(file):
    try:
        with open(file, "r") as f:
            lines = f.readlines()
            return len(lines)

    except FileNotFoundError:
        print("File not found!")
        return None

def special_character_counter(file):
    try:
        count = 0
        with open(file, "r") as f:
            for line in f:
                for char in line:
                    if not char.isalnum() and not char.isspace():
                        count += 1
        return count

    except FileNotFoundError:
        print("File not found!")
        return None
    except Exception as e:
        print("Something went wrong:", e)
        return None
    

file = input("Enter file path: ")
words = word_counter(file)
lines = line_counter(file)
special_chars = special_character_counter(file)

if (words != None) and (lines != None) and (special_chars != None):
    print(f"Total number of words: {words}")
    print(f"Total number of lines: {lines}")
    print(f"Total number of special characters: {special_chars}")
