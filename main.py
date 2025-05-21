from stats import count_words, sort_char_dictionary
from stats import count_characters
import sys
import os

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()

    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        file = sys.argv[1]

    book_text = get_book_text(file)
    num_words = count_words(book_text)
    num_chars = count_characters(book_text)
    char_list = sort_char_dictionary(num_chars)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in char_list:
        if char[0].isalpha():
            print(f"{char[0]}: {char[1]}")
    print("============= END ===============")

main()
