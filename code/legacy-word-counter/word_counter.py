from collections import Counter

from tabulate import tabulate


def most_common_words(filename, n=5):
    """
    Find the n most common words in a file. Return a list of (word, count) pairs
    """
    counter = Counter()
    for line in open(filename):
        for word in line.split():
            counter[word.lower()] += 1
    return counter.most_common(n)


def main():
    words = most_common_words("../data/stevenson_clean.txt")
    print(tabulate(words, headers=["Word", "Count"]))


if __name__ == "__main__":
    main()
