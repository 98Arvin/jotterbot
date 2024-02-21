def main():
    book_path = "books/frankenstein.txt"
    string = book_string(book_path)
    total_words = get_word_count(string)
    char_count = duplicate_char_count(string)
    sorted_list = get_sorted_list(char_count)

    print(f"Book: {book_path}")
    print(f"Word count: {total_words}")
    print()
    print(f"===REPORT===")
    tldr(sorted_list)
    print(f"===END===")

def get_word_count(text):
    words = text.split()
    return len(words)

def book_string(path):
    with open("books/frankenstein.txt") as f:
        return f.read()

def duplicate_char_count(text):
    duplicates = {}
    for char in text:
        if char.lower() in duplicates:
            duplicates[char.lower()] += 1
        else:
            duplicates[char.lower()] = 1
    return duplicates

def get_sorted_list(dictionary):
    def sorting(d):
        return d["num"]

    sorted_dict = []
    for char in dictionary:
        sorted_dict.append({"char": char, "num": dictionary[char]})
    sorted_dict.sort(reverse=True, key=sorting)
    return sorted_dict

def tldr(sorted_list):
    for char in sorted_list:
        if char["char"].isalpha() == True:
            print(f"Character {char['char']} was found {char['num']} times")

main()