import collections


def word_count(phrase):
    clean_phrase = phrase.lower().replace('_', ' ').replace(',', ' ')
    alphanum_words = ''.join(filter(lambda c: c.isalnum() or c.isspace() or c == '\'', clean_phrase)).split()
    stripped_words = map(lambda word: word.strip('\''), alphanum_words)
    return collections.Counter(stripped_words)

