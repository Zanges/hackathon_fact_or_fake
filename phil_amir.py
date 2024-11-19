import random
from colorama import Fore, Style, init

import pretty_print
from header import header

init(autoreset=True)

def run_question(fake_passage, passage):
    # print(Fore.LIGHTCYAN_EX + "-------------------------------------------")
    # print(Fore.LIGHTCYAN_EX + "-------- Welcome to our Wiki Game ---------")
    # print(Fore.LIGHTCYAN_EX + "Try to guess which one is the fake passage!")
    # print(Fore.LIGHTCYAN_EX + "-------------------------------------------")
    header()


    passages = [passage, fake_passage]
    random.shuffle(passages)

    pretty_print.print_paragraph_with_linebreaks(Fore.LIGHTYELLOW_EX + "1. " + passages[0])
    print()
    pretty_print.print_paragraph_with_linebreaks(Fore.LIGHTYELLOW_EX + "2. " + passages[1])

    while True:
        try:
            question = Fore.LIGHTGREEN_EX + "Which paragraph is fake?:"
            options = ["Paragraph", "Paragraph"]
            user_input = pretty_print.get_player_answer(question, options)
            print(user_input)
            if (user_input == 0 and passages[0] == fake_passage) or (
                user_input == 1 and passages[1] == fake_passage
            ):
                print(Fore.GREEN + Style.BRIGHT + "Correct! You earn 10 points.")
                return 10
            elif user_input in [0, 1]:
                print(Fore.RED + Style.BRIGHT + "Incorrect! Better luck next time...")
                return 0
            else:
                print(Fore.RED + "Invalid input. Please choose only 1 or 2.")
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a number (1 or 2).")


# real_passage = "The Eiffel Tower is located in Paris and was completed in 1889."
# fake_passage = "The Eiffel Tower was originally constructed in Tokyo before being moved to Paris."
# run_question(fake_passage,real_passage)