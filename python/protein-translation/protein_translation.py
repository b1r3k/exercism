methionine = 'Methionine'
phenylalanine = 'Phenylalanine'
leucine = 'Leucine'
serine = 'Serine'
tyrosine = 'Tyrosine'
cysteine = 'Cysteine'
tryptophan = 'Tryptophan'
stop = 'STOP'

condon_to_protein = {
    'AUG': methionine,
    'UUU': phenylalanine,
    'UUC': phenylalanine,
    'UUA': leucine,
    'UUG': leucine,
    'UCU': serine,
    'UCC': serine,
    'UCA': serine,
    'UCG': serine,
    'UAU': tyrosine,
    'UAC': tyrosine,
    'UGU': cysteine,
    'UGC': cysteine,
    'UGG': tryptophan,
    'UAA': stop,
    'UAG': stop,
    'UGA': stop
}


def proteins(strand):
    proteins_seq = []
    condon_len = 3
    codons = [strand[pos:pos+condon_len] for pos in range(0, len(strand), condon_len)]
    for codon in codons:
        protein = condon_to_protein[codon]
        if protein is stop:
            break
        proteins_seq.append(protein)
    return proteins_seq
