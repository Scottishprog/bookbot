def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    letter_count = get_num_letters(text)
    sorted_letter_count = format_num_letters(letter_count)

    # print out report...
    print("--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print(" ")
    for letter in sorted_letter_count:
        if letter["letter"].isalpha():
            print(f"The {letter["letter"]} was found {letter["count"]} times")
    print("--- End report of {book_path} ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_num_words(text):
    words = text.split()
    return len(words)


def get_num_letters(text):
    lowered_text = text.lower()
    letter_count = dict()
    for letter in lowered_text:
        if letter not in letter_count:
            letter_count[letter] = 1
        else:
            letter_count[letter] += 1
    return letter_count


def sort_on(sort_key):
    return sort_key["letter"]


def format_num_letters(num_letters):
    sorted_list = []
    for letr, cnt in num_letters.items():
        sorted_list.append({"letter": letr, "count": cnt})
    sorted_list.sort(key=sort_on, reverse=False)
    return sorted_list


main()
