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


def sort_on(d):
    return d["num"]


def num_letters_to_sorted_letters(num_letters):
    sorted_letters = []
    for char in num_letters:
        sorted_letters.append({"char": char, "num": num_letters[char]})
    sorted_letters.sort(reverse=True, key=sort_on)
    return sorted_letters
