import re
print(""""
Welcome to Mad Libs
Lets Play a game
Type in two adjectives and one noun
A Madlib response will be displayed.
**An adjective denotes a descriptive word that illustrates the noun used in a sentence.
**A noun is a word that connotes a particular name, place, idea, or object.
      """)


def read_template(path):
    try:
        with open(path,'r') as story:
            output = story.read().strip()
            return output
    except FileNotFoundError:
        raise FileNotFoundError

    
def parse_template(pre_string):
    stripped_string = ""
    parts = []
    content = False
    characters = ""

    for letter in pre_string:
        if letter == "{":
            stripped_string += letter
            content = True
            characters = ""
        elif letter == "}":
            stripped_string += letter
            content = False
            parts.append(characters)
        elif content:
            characters += letter
        else:
            stripped_string += letter

    return stripped_string, tuple(parts)


def merge(string, user_input):
    story = string.format(*user_input)
    return story