def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Unequal strands")
    pairs = zip(strand_a, strand_b)
    errors = filter(lambda pair: pair[0] != pair[1], pairs)
    return len(errors)
