import random

from pretty_print import get_player_answer

YES_NO_CHOICES = ["yes", "no"]


def wants_crash() -> bool:
    """Ask User for to call a crash"""
    use_crash = get_player_answer(
        "Do you want to use the ultimate crash? (yes/no): ", YES_NO_CHOICES
    )
    if use_crash == 0:
        return True
    return False


def choose_crash():
    """Ask User to choose crash"""
    crash_choices = [crash["label"] for crash in CRASH_LIST]
    crash_choice = get_player_answer("Choose a crash: ", crash_choices)
    return CRASH_LIST[crash_choice]["function"]


def replace_nth_word(text, n, word_1, word_2) -> str:
    """Replace nth word with word_1 and every n*2th word with word_2"""
    words = text.split()
    word_count = len(words)
    for i in range(word_count):
        if i % n == 0:
            words[i] = word_1
        if i % n * 2 == 0:
            words[i] = word_2
    return " ".join(words)


def all_o_crash(text) -> str:
    """Crash to replace all e,u,i,a's with o's"""
    return text.replace("e", "o").replace("u", "o").replace("i", "o").replace("a", "o")


def lower_upper_crash(text) -> str:
    """Crash to flip upper case and lower case"""
    return "".join([
        letter.lower() if letter != letter.lower() else letter.upper()
        for letter in text
    ])


def dogs_and_cats_crash(text) -> str:
    """Don't eat the cats and dogs!"""
    return replace_nth_word(text, 4, "dog", "cat")


def eeeh_crash(text) -> str:
    """Crash to replace every 5th word with eeeh or 10th word with mhhh"""
    return replace_nth_word(text, 5, "eeeh", "mhhh")


def hide_crash(text) -> str:
    """Crash to replace every 3rd word with ***** or ####"""
    return replace_nth_word(text, 3, "*****", "####")


CRASH_LIST = [
    {"label": "Oooooh", "function": all_o_crash},
    {"label": "Flip Case", "function": lower_upper_crash},
    {"label": "Don't eat the cat's and dog's", "function": dogs_and_cats_crash},
    {"label": "Eeeeh", "function": eeeh_crash},
    {"label": "***** ####", "function": hide_crash},
]