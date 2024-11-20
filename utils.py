import os
import random


def clear_console() -> None:
    """Clear Terminal"""
    if os.name == "nt":  # Windows
        os.system("cls")
    else:  # macOS/Linux
        os.system("clear")


def replace_nth_word(text: str, n, word_1: str, word_2: str) -> str:
    """Replace nth word with word_1 and every n*2th word with word_2"""
    words = text.split()
    word_count = len(words)
    for i in range(word_count):
        if i % (n * 2) == 0:
            words[i] = word_1
        elif i % n == 0:
            words[i] = word_2

    return " ".join(words)


def add_nth_word(text: str, n: int, word_1: str, word_2: str) -> str:
    """Add word_1 and word_2 to text on every nth word"""
    words = text.split()
    word_count = len(words)
    for i in range(word_count):
        if i % (n * 2) == 0:
            words[i] += word_1
        elif i % n == 0:
            words[i] += word_2
    return " ".join(words)


def random_char_case(letter: str) -> str:
    """Get random char in upper or lower case"""
    random_int = random.randint(0, 1)
    if random_int == 1:
        return letter.upper()
    return letter.lower()


def replace_region(text: str, n: int, k: int, sign: str) -> str:
    """Replace area (n = index, k = length) of text with sign"""
    number_idx = len(text) // n

    start_idxs = []
    for i in range(number_idx):
        random_n = random.randint(-(n - k), (n - k))
        start_idx = n * i + random_n
        start_idxs.append(start_idx)

    replaced_idxs = []
    for index in start_idxs:
        for i in range(k):
            replaced_idxs.append(index + i)

    new_text = ""
    for i, char in enumerate(text):
        if i in replaced_idxs:
            new_text += sign
        else:
            new_text += char

    return new_text


def get_terminal_width() -> int:
    """try to find the terminal width"""
    try:
        return os.get_terminal_size().columns
    except OSError:
        return 180
