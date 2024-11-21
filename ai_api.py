import os

import dotenv
from openai import OpenAI

import request_wiki_categories

dotenv.load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

DIFFICULTIES = {
    "easy": {
        "temperature": 0.99,
        "prompt": """
            You are an AI, that is part of a game, tasked with creating an obvious, fake information about the topic. 
            Your goal is to write a new passage about the same topic as the original one:
            The player chose the following difficulty: easy
            - It should contain obvious false information.
            - The difficulty should determine how obvious and stupid the fake one is to spot.
    
            Important:
            - The rewritten passage **must not exceed the word or character count** of the original excerpt.
            - Prioritize concise phrasing and efficient language while maintaining clarity and formal tone.
    
            Now, rewrite the provided passage adhering strictly to the guidelines above.
            """,
    },
    "hard": {
        "temperature": 0.5,
        "prompt": """
            You are an AI, that is part of a game, tasked with creating a fake passage based on a provided excerpt. 
            Your goal is to write a new passage about the same topic as the original one:
            The player chose the following difficulty: hard
            - Believable details that mimic Wikipedia's formal style.
            - Coherence and proper structure while avoiding obvious gibberish.
            - It should contain obvious false information.
            - The difficulty should determine how obvious and stupid the fake one is to spot.
    
            Important:
            - The rewritten passage **must not exceed the word or character count** of the original excerpt.
            - Prioritize concise phrasing and efficient language while maintaining clarity and formal tone.
    
            Now, rewrite the provided passage adhering strictly to the guidelines above.
            """,
    },
}


def get_fake_passage(passage: str, difficulty: str) -> str:
    """Generate a fake passage based on the provided passage and difficulty level."""
    print("\nGenerating passage...\n")
    if not passage:
        raise ValueError("passage must not be empty.")
    if difficulty not in DIFFICULTIES:
        raise ValueError(f"difficulty must be one of {list(DIFFICULTIES.keys())}.")

    client = OpenAI()
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        temperature=DIFFICULTIES[difficulty]["temperature"],
        messages=[
            {
                "role": "system",
                "content": [
                    {"type": "text", "text": DIFFICULTIES[difficulty]["prompt"]}
                ],
            },
            {"role": "user", "content": [{"type": "text", "text": passage}]},
        ],
    )

    if completion.choices[0].finish_reason == "stop":
        fake_passage = completion.choices[0].message.content
        return fake_passage
    else:
        raise Exception(
            f"The completion was not successful.\n" f"DUMP:\n" f"{completion}"
        )


def main():
    import pretty_print

    dev_passage = request_wiki_categories.get_article_content(
        request_wiki_categories.get_random_valid_title(
            "List of video games considered the best"
        )
    )[1]
    easy_fake_passage = get_fake_passage(dev_passage, "easy")
    medium_fake_passage = get_fake_passage(dev_passage, "medium")
    hard_fake_passage = get_fake_passage(dev_passage, "hard")
    pretty_print.print_paragraph_with_linebreaks(f"Original Passage:\n{dev_passage}")
    print()
    pretty_print.print_paragraph_with_linebreaks(
        f"Easy Fake Passage:\n{easy_fake_passage}"
    )
    print()
    pretty_print.print_paragraph_with_linebreaks(
        f"Medium Fake Passage:\n{medium_fake_passage}"
    )
    print()
    pretty_print.print_paragraph_with_linebreaks(
        f"Hard Fake Passage:\n{hard_fake_passage}"
    )


if __name__ == "__main__":
    main()
