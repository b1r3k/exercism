def dna_to_rna(nucleotide):
    mapping = {
        'G': 'C',
        'C': 'G',
        'T': 'A',
        'A': 'U',
    }
    return mapping[nucleotide]


def to_rna(dna_strand):
    translated = map(dna_to_rna, list(dna_strand))
    return ''.join(translated)
