from colorama import Fore, Style
from podium import display_podium


def final(players):

    trophy = """
##   ##    ####   ###  ##  ###  ##  ### ###  ### ##    ## ##     .-=========-.
##   ##     ##      ## ##    ## ##   ##  ##   ##  ##  ##   ##    \'-=======-'/ 
##   ##     ##     # ## #   # ## #   ##       ##  ##  ####       _|   .=.   |_ 
## # ##     ##     ## ##    ## ##    ## ##    ## ##    #####    ((|  {{1}}  |)) 
# ### #     ##     ##  ##   ##  ##   ##       ## ##       ###    \|   /|\   |/  
 ## ##      ##     ##  ##   ##  ##   ##  ##   ##  ##  ##   ##     \__ '`' __/   
##   ##    ####   ###  ##  ###  ##  ### ###  #### ##   ## ##        _`) (`_     
                                                                  _/_______\_   
                                                                 /___________\  

"""
    print(trophy)
    # return trophy


# trophy_ascii = final(players)
# print(trophy_ascii)
    display_podium(players)

    print("\n" + Fore.YELLOW + " " * 10 + "🏆 Congratulation To All Players 🏆" + Style.RESET_ALL + "\n")
    print(Fore.LIGHTGREEN_EX + "Thanks for playing our game!\nHope you had some fun playing it\nWe had a lot of fun creating it\n" + Style.RESET_ALL)
    print(Fore.LIGHTGREEN_EX + "Don´t eat cats and dogs!\n" + Fore.LIGHTGREEN_EX)
    print("____________________________________________")
    print(Fore.LIGHTGREEN_EX + "Creators: Dominik, Philipp, Amir, Jorge, Lea, \n" + Style.RESET_ALL)

final(players)