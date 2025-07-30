def repeat_string(string, number):
    return string * number  # fixed


class Car:
    def __init__(self, name="", fuel=0):
        self.name = name
        self.fuel = fuel

    def __str__(self):
        return f"{self.name}, {self.fuel}"

# Add tests
car = Car("Test", 42)
assert car.fuel == 42
car2 = Car("Another", 0)
assert car2.fuel == 0


def is_long_word(word, length=5):
    """Determine if the word is at least as long as the length supplied.

    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    """
    return len(word) >= length


def format_sentence(phrase):
    """Return a phrase as a sentence starting with capital and ending with a period.

    >>> format_sentence("hello")
    'Hello.'
    >>> format_sentence("It is a test.")
    'It is a test.'
    >>> format_sentence("Already.")
    'Already.'
    """
    sentence = phrase.strip().capitalize()
    if not sentence.endswith('.'):
        sentence += '.'
    return sentence


if __name__ == '__main__':
    import doctest
    doctest.testmod()
