from collections import Counter

def word_count(given):
    words = given.split()
    word_count = Counter(words)
    return word_count