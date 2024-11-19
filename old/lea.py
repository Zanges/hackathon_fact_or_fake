from giorgio import get_random_article_text
import random


# function currently outdated
# def get_passage(article_text):
#     """gets a text and returns a passage"""
#
#     sections = article_text.split('\n\n')
#     useful_passages = [section for section in sections if len(section) > 100]
#     passage = random.choice(useful_passages)
#     return passage

original_passage = get_random_article_text()["summary"]

#currently per sentence
# def shrink_text(passage, original_passage):
#     """ gets passage and returns a smaller version of it"""
#     sections = passage.split('.')
#     if len(sections) > 1:
#         smaller_passage = '.'.join(sections[:-1])
#     else:
#         smaller_passage = passage
#     return smaller_passage.strip()
#
# def shrink_text(passage, original_passage):
#     if len(passage) == len(original_passage):
#         passage = original_passage
#
#     sections = passage.split('.')
#     if len(sections) > 1:
#         smaller_passage = '.'.join(sections[:-1])
#     else:
#         smaller_passage = passage
#     return smaller_passage.strip()
#
#
#
#
# #currently per sentence
# def enlarge_text(passage, original_passage):
#     """ gets passage and return a larger version of it"""
#     current_sections = passage.split('.')
#     original_sections = original_passage.split('.')
#
#     if len(current_sections) < len(original_sections):
#         expanded_passage = '.'.join(original_sections[:len(current_sections) + 1])
#     else:
#         expanded_passage = passage
#     return expanded_passage.strip()

def text_size_choice(passage):
    """Menu for shrinking or enlarging the upcoming text"""
    menu_actions = {
        "1": shrink_text,
        "2": enlarge_text,
    }

    select = input("Choose an option -> 1 to shrink or 2 to enlarge): ").strip()

    if select in menu_actions:
        action = menu_actions[select]
        return action(passage)
    else:
        raise ValueError("Please select 1 or 2")


original_passage = get_random_article_text()["summary"]
passage = original_passage


def shrink_text(passage):
    """Shortens the passage by removing the last sentence"""
    sections = passage.split('.')
    if len(sections) > 1:
        smaller_passage = '.'.join(sections[:-1])
    else:
        smaller_passage = passage
    return smaller_passage.strip()


def enlarge_text(passage):
    """Expands the passage by adding the next sentence from the original"""
    current_sections = passage.split('.')
    original_sections = original_passage.split('.')

    if len(current_sections) < len(original_sections):
        expanded_passage = '.'.join(original_sections[:len(current_sections) + 1])
    else:
        expanded_passage = passage
    return expanded_passage.strip()