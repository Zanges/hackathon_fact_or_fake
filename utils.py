import os


def clear_console():
    """Clear Terminal"""
    if os.name == "nt":  # Windows
        os.system("cls")
    else:  # macOS/Linux
        os.system("clear")
