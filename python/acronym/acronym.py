
def abbreviate(sentence):
    words = filter(lambda w: len(w), sentence.replace('-', ' ').split(' '))
    return ''.join(map(lambda w: w[0].upper(), words))
