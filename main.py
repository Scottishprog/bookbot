from stats import (get_num_words, num_letters_to_sorted_letters, get_num_letters )
import sys


def main():
    if len(sys.argv) > 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    text = get_book_text(book_path)
    num_words = get_num_words(text)
    letter_count = get_num_letters(text)
    sorted_letter_count = num_letters_to_sorted_letters(letter_count)

    # print out report...
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ---------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for letter in sorted_letter_count:
        if letter["char"].isalpha():
            print(f"{letter['char']}: {letter['num']}")
    print(f"============= END ===============")


def get_book_text(path):
    with open(path) as f:
        return f.read()


def sort_on(sort_key):
    return sort_key["letter"]


def format_num_letters(num_letters):
    sorted_list = []
    for letr, cnt in num_letters.items():
        sorted_list.append({"letter": letr, "count": cnt})
    sorted_list.sort(key=sort_on, reverse=False)
    return sorted_list


main()
