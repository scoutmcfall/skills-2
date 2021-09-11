"""Skills 2: dicts.py

Complete the following functions. To get a better idea of how each function
should behave, see the examples in test_dicts.py.
"""


def count_words(phrase):
    """Count the words in a string.

    This function doesn't handle punctuation so 'hello!' and 'hello'
    are two different words. It also doesn't handle captialization so
    'Hello' and 'hello' are two different words as well.
    """
    word_count = len(phrase.split())
    words = phrase.split()
    word_count_dict = {}
    # sum_count = []
    for word in words:
        key = word
        word_count_dict[key] = 1
        word_count_dict[key] = word_count_dict.get(key,+1)
    # for key, value in word_count_dict:
    #     value.append(sum_count)

    return word_count_dict

    # TODO: replace this with your code


MELONS = [
    ("honeydew", 2.5),
    ("cantaloupe", 2.5),
    ("watermelon", 2.95),
    ("musk", 3.25),
    ("crenshaw", 3.25),
    ("christmas", 14.25),
]


def get_melons_at_price(price):
    """Return a set with the names of melons being sold at the given price.

    This will return the names of melons from MELONS. MELONS is a list
    of tuples that have (melon_name, price).

    If there are no melons being sold at the given price it returns an
    empty set.
    """
    melon_names = []
    melon_set = set(melon_names)
    for melon in MELONS:
        if price in melon:
            melon_names.append(melon)
    return melon_set

    # melon_set = {}
    # for melon in MELONS:
    #     MELONS[melon] = MELONS.get(price, [])
    #     melon_set.add(melon)
    # return melon_set
    # TODO: replace this with your code


ENG_PIRATE_LOOKUP = {
    "sir": "matey",
    "hotel": "fleabag inn",
    "student": "swabbie",
    "man": "matey",
    "professor": "foul blaggart",
    "restaurant": "galley",
    "your": "yer",
    "excuse": "arr",
    "students": "swabbies",
    "are": "be",
    "restroom": "head",
    "my": "me",
    "is": "be",
}


def translate_to_pirate_talk(phrase):
    """Return a phrase in pirate talk.

    Given an English phrase, use ENG_PIRATE_LOOKUP to translate
    words to pirate talk. Words that aren't listed in ENG_PIRATE_LOOKUP
    should not be translated and should pass through unchanged.

    The given phrase will be normalized so it will never contain punctuation
    and will only consist of lowercased letters.
    """
    words = phrase.split() #split up the input phrase into a list of words
    pirate_phrase = [] #create a place for the final phrase to live
    
    for word in words:
        if ENG_PIRATE_LOOKUP[word] == ENG_PIRATE_LOOKUP.get(word, []):
            pirate_phrase.append(ENG_PIRATE_LOOKUP[word])
        # if word in ENG_PIRATE_LOOKUP:
        #     pirate_phrase.append(ENG_PIRATE_LOOKUP[word])
        else:
            pirate_phrase.append(word)
    pirate_string = str(pirate_phrase)
    #pirate_phrase.join("")
    return pirate_string
    # TODO: replace this with your code


def create_word_chain(words):
    """Return a sequence of words arranged according to the rules below.

    The sequence starts with the first word in the given list. The
    next word will start with the last letter of the preceding word.
    For example, these are all valid sequences of words:

        zoo, octos, sour, racket
        cute, etcetera, antsy, yak, karat

    Sometimes you'll get a word where there are multiple candidates
    for the next word. For example, if our list of words contains:

        noon, naan, nun

    ...then the first word in the sequence is 'noon':

        noon

    ...the next word should be the *first* word that starts with 'n'.
    So, even though 'naan' and 'nun' both start with 'n', the next
    word should be 'naan' because 'naan' appears before 'nun'. The
    final sequence of words will be:

        noon, naan, nun

    The sequence will continue in this fashion until it runs out of
    words or it can't find words that'll fit the pattern.
    """
    #this broke the test also!
    sequence = [words[0]]
    #((sequence[0])[-1]) = ((sequence[1])[0]) #the second word starts with the last letter of the first word
    #make a dictionary of first letter:word pairs
    # word_dict = {}
    # for word in words:
    #     key = word
    #     word_dict[key] = word[0]
    # for word in sequence:
    #     word_dict[word] = word_dict.get(word[-1], [])
    #     sequence.append("whichever word comes next")
    #SOMETHING I did here broke the test
    #make a dictionary of (last letter: word) pairs?
    # word_dict = {}
    # for word in words:
    #     key = word[-1]
    #     word_dict[key] = word
    # word_chain = [words[0]]
    # for word in word_chain:
    #     word_dict[word[-1]] = word_dict.get(word[-1],[])
    #     word_chain.append(word_dict[word[-1]])
    # return words
    # TODO: replace this with your code


if __name__ == "__main__":
    import sys
    from pathlib import Path

    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        try:
            import pytest

            pytest.main([f"test_{Path(__file__).name}"])
        except ModuleNotFoundError:
            print("Unable to run tests because 'pytest' wasn't found :(")
            print("Run the command below to install pytest:")
            print()
            print("    pip3 install pytest")
