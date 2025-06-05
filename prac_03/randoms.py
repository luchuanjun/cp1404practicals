import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"

def generate_word(word_format):
    """Generate a random word based on the format:
    'c' = consonant, 'v' = vowel
    """
    word = ""
    for kind in word_format:
        if kind == "c":
            word += random.choice(CONSONANTS)
        elif kind == "v":
            word += random.choice(VOWELS)
        else:
            # if format contains other chars, add as is or skip
            word += kind
    return word

def main():
    word_format = "ccvcvvc"  # example format
    word = generate_word(word_format)
    print(f"Generated word: {word}")
if __name__ == "__main__":
    main()
