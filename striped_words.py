import re
from string import ascii_lowercase

VOWELS = "aeiouy"


def checkio(text):
    words = re.findall(re.compile(r'\b[^\W\d]{2,}\b'), text.lower())
    transl_to = ''.join('1' if char in VOWELS else '0' for char in ascii_lowercase)
    translator = str.maketrans(ascii_lowercase, transl_to)
    translated_words = (word.translate(translator) for word in words)

    count = 0
    for word in translated_words:
        if re.search(r'(00|11)', word):
            count += 1

    return len(words) - count

if __name__ == '__main__':
    assert checkio("My name is ...") == 3, "All words are striped"
    assert checkio("Hello world") == 0, "No one"
    assert checkio("A quantity of striped words.") == 1, "Only of"
    assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"
