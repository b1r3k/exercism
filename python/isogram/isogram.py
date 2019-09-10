from collections import Counter


def is_isogram(string):
    c = Counter(string.lower())
    most_common = c.most_common(3)
    for c, count in most_common:
        if c not in ' -' and count > 1:
            return False
    return True

