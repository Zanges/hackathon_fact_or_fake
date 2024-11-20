from pretty_print import get_player_answer
from utils import replace_nth_word, random_char_case, add_nth_word, replace_region

YES_NO_CHOICES = ["yes", "no"]


def wants_crash() -> bool:
    """Ask User if they want to use the ultimate crash"""
    use_crash = get_player_answer(
        "Do you want to use the ultimate crash? (yes/no): ", YES_NO_CHOICES
    )
    if use_crash == 0:
        return True
    return False


def choose_crash() -> callable:
    """Ask User to choose crash"""
    crash_choices = [crash["label"] for crash in CRASH_LIST]
    crash_choice = get_player_answer("Choose a crash: ", crash_choices)
    return CRASH_LIST[crash_choice]["function"]


def all_o_crash(text: str) -> str:
    """Crash to replace all e,u,i,a's with o's"""
    return text.replace("e", "o").replace("u", "o").replace("i", "o").replace("a", "o")


def lower_upper_crash(text: str) -> str:
    """Crash to flip letter randomly upper and lower case"""
    return "".join([random_char_case(letter) for letter in text])


def dogs_and_cats_crash(text: str) -> str:
    """Don't eat the cats and dogs!"""
    return replace_nth_word(text, 4, "dog", "cat")


def think_crash(text: str) -> str:
    """Crash to replace every 5th word with eeeh or 10th word with mhhh"""
    return add_nth_word(text, 5, ", eeeh", ", mhhh")


def classified_crash(text: str) -> str:
    """Crash to replace every 3rd word with ***** or ####"""
    return replace_region(text, 80, 12, "▇▇")


def reverse_crash(text: str) -> str:
    words = text.split()
    word_count = len(words)
    for i in range(word_count):
        if i % 10 == 0:
            words[i] = words[i][::-1]
    return " ".join(words)


CRASH_LIST = [
    {"label": "Oooooh", "function": all_o_crash},
    {"label": "Flip Case", "function": lower_upper_crash},
    {"label": "Don't eat the cat's and dog's", "function": dogs_and_cats_crash},
    {"label": "Thinking ...", "function": think_crash},
    {"label": "!CLASSIFIED!", "function": classified_crash},
    {"label": "reverse", "function": reverse_crash},
]
