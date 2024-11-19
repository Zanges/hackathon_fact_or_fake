def print_paragraph_with_linebreaks(paragraph: str, line_length: int = 80, indent: int = 0) -> None:
    """
    Print a paragraph with line breaks to ensure that no line exceeds the specified line length.
    The paragraph is indented by the specified number of spaces.

    :param paragraph: The paragraph to print.
    :param line_length: The maximum length of a line.
    :param indent: The number of spaces to indent the paragraph.
    """
    if not paragraph:
        return
    if line_length <= 0:
        raise ValueError("line_length must be greater than 0")
    if indent < 0:
        raise ValueError("indent must be greater than or equal to 0")

    words = paragraph.split()
    current_line_length = 0
    print((" " * indent) + words[0], end=" ")
    for word in words[1:]:
        if current_line_length + len(word) + 1 <= line_length:
            print(word, end=" ")
            current_line_length += len(word) + 1
        else:
            print("\n" + (" " * indent) + word, end=" ")
            current_line_length = len(word)
    print()


def get_player_answer(question: str, options: list[str], silent_error: bool = False) -> int:
    """
    Get the player's answer to a multiple-choice question.

    :param question: The question to ask the player.
    :param options: The list of options to choose from.
    :param silent_error: Whether to suppress error messages.
    :return: The index of the chosen option.
    """
    if not question:
        raise ValueError("question must not be empty.")
    if not options:
        raise ValueError("options must not be empty.")
    if not all(isinstance(option, str) for option in options):
        raise ValueError("options must contain only strings.")
    if not all(options):
        raise ValueError("options must not contain empty strings.")

    print("-" * len(question))
    print(question)
    answer_lines = ["", "", ""]
    for i, option in enumerate(options, start=1):
        text = f"{i}. {option}"
        horizontal_line = "─" * (len(text) + 2)
        answer_lines[0] += f"╭{horizontal_line}╮  "
        answer_lines[1] += f"│ {text} │  "
        answer_lines[2] += f"╰{horizontal_line}╯  "
    for line in answer_lines:
        print(line)
    while True:
        try:
            answer = int(input(""))
            if 1 <= answer <= len(options):
                return answer - 1
            else:
                if not silent_error:
                    print(f"Input must be in range 1 - {len(options)}")
        except ValueError:
            if not silent_error:
                print("Input must be a number.")


def test_ppwl():
    paragraph = "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet."
    print_paragraph_with_linebreaks(paragraph)
    print("=================")
    print_paragraph_with_linebreaks(paragraph, line_length=40)
    print("=================")
    print_paragraph_with_linebreaks(paragraph, line_length=40, indent=4)


def test_gpa():
    question = "Choose between 1 or 2 and hit enter!"
    options = ["FACT", "FAKE"]
    answer = get_player_answer(question, options)
    print(f"Player chose option {answer + 1}")


def main():
    test_ppwl()
    test_gpa()


if __name__ == "__main__":
    main()
