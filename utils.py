import os


def clear_console():
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
        if i % n == 0:
            words[i] = word_1
        if i % n * 2 == 0:
            words[i] = word_2
    return " ".join(words)
