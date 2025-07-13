"""
Word occurrences counter
Estimate: 25 minutes
Actual:   35 minutes
"""


def main():
    text = input("Text: ")
    word_counts = {}
    words = text.split()

    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1

    max_length = max(len(word) for word in word_counts.keys())
    for word, count in sorted(word_counts.items()):
        print(f"{word:{max_length}} : {count}")


if __name__ == "__main__":
    main()