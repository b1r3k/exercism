from collections import Counter


def is_pangram(sentence):
    clean_sentence = filter(lambda char: char.isalpha(), sentence.replace(' ', '').lower())
    c = Counter(clean_sentence)
    unique_elements = c.most_common()
    return len(unique_elements) == 26

