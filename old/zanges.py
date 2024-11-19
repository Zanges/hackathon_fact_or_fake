import dotenv
from openai import OpenAI
import os


dotenv.load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


def get_fake_passage(passage):
    client = OpenAI()
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": [
                    {
                        "type": "text",
                        "text": """
                        You are an AI agent engaged in a game where your mission is to create a fake passage based on a section from a Wikipedia article. Your task is to generate a passage that matches the topic but does not copy the original text exactly. It should be both believable and easily identifiable as a fake, allowing players to spot it without difficulty. Avoid simple tweaks like altering dates or places; instead, focus on rephrasing and reimagining the content while maintaining the overall style. For example, if the original discusses "the invention of the steam engine in the 18th century," your version could describe "the creation of the wind-powered carriage in the 1700s," altering key details to signal its inauthenticity effectively. come up with at least one clear halucination.
                        """
                    }
                ]
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": passage
                    }
                ]
            }
        ]
    )
    if completion.choices[0].finish_reason == "stop":
        fake_passage = completion.choices[0].message.content
        return fake_passage
    else:
        raise Exception(f"The completion was not successful.\nDUMP:\n{completion}")


def main():
    dev_passage = "Globally, CNN programming has aired through CNN International, seen by viewers in over 212 countries and territories.[16] Since May 2019, however, the US domestic version has absorbed international news coverage in order to reduce programming costs. The American version, sometimes referred to as CNN (US), is also available in Canada, and some islands in the Caribbean. CNN also licenses its brand and content to other channels, such as CNN-News18 in India. In Japan it broadcasts CNNj which started in 2003, with simultaneous translation in Japanese.[17]"
    fake_passage = get_fake_passage(dev_passage)
    print(f"Original Passage:\n{dev_passage}\n")
    print(f"Fake Passage:\n{fake_passage}")


if __name__ == "__main__":
    main()