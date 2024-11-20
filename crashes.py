import random

from pretty_print import get_player_answer


YES_NO_CHOICES = ["yes", "no"]


def wants_crash() -> bool:
    """Ask User for to call a crash"""
    use_ultimate = get_player_answer("Do you want to use the ultimate crash? (yes/no): ", YES_NO_CHOICES)
    if use_ultimate == 0:
        return True
    return False


def random_crash(text) -> str:
    """Get a random crash"""
    crashes = (
        reverse_crash,
        replace_crash,
        lower_upper_crarsh,
        third_word_crash,
    )
    crash = random.choice(crashes)
    return crash(text)


def choose_crash():
    """Ask User to choose crash"""
    crash_choices = [crash["label"] for crash in CRASH_LIST]
    crash_choice = get_player_answer("Choose a crash: ", crash_choices)
    return CRASH_LIST[crash_choice]["function"]


def reverse_crash(text) -> str:
    """Crash to reverse text"""
    return text[::-1]


def replace_crash(text) -> str:
    """Crash to replace all e's to o's"""
    return text.replace("e", "o")


def lower_upper_crarsh(text) -> str:
    return "".join([
        letter.lower() if letter != letter.lower() else letter.upper()
        for letter in text
    ])


def third_word_crash(text) -> str:
    words = text.split()
    word_count = len(text.split())
    for i in range(word_count):
        if i % 3 == 0:
            words[i] = "eeehm"
    return " ".join(words)


CRASH_LIST = [
    {
        "label": "reverse",
        "function": reverse_crash
    },
    {
        "label": "replace",
        "function": replace_crash
    },
    {
        "label": "lower_upper",
        "function": lower_upper_crarsh
    },
    {
        "label": "third_word",
        "function": third_word_crash
    }
]

# print(third_word_crash(article_text))
# print(lower_upper_crarsh(article_text))
# print(replace_crash(article_text))
