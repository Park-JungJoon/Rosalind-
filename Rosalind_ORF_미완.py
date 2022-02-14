def transcription(a):
    b=a.replace('T','Z')
    c=b.replace('G','X')
    d=c.replace('A', 'T')
    e=d.replace('C', 'G')
    f=e.replace('Z', 'A')
    g=f.replace('X','C')
    h=g.replace('T','U')
    i=list(h)
    i.reverse()

def translate(a):
    RNA_seq = a
    codon_table ={'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L', 'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S', 'UAU': 'Y', 'UAC': 'Y', 'UAA': '*', 'UAG': '*', 'UGU': 'C', 'UGC': 'C', 'UGA': '*', 'UGG': 'W', 'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L', 'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P', 'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q', 'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R', 'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M', 'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T', 'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K', 'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R', 'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V', 'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A', 'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E', 'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'}
    start_codon = RNA_seq.find('AUG')
    AA_seq = []
    i = start_codon
    while i < len(RNA_seq)-2:
        codon = RNA_seq[i:i+3]
        AA = codon_table[codon]
        i+=3
        AA_seq.append(AA)
    return ''.join(AA_seq)

def OpenReadingFrame(b):
    Msite = ''
    end_site = ''
    import numpy as np 
    AAseq = b
    for m in re.finditer('AUG', AAseq):



text = 'Allowed Hello Hollow'
print [n for n in xrange(len(text)) if text.find('ll',n)==n]
