def rev_comp(fa):
    '''
    Give transript and reversed complementary transcript
    '''
    fa_transcript = ''
    for i in range(len(fa)):
        index = -(i+1)
        if fa[index] == 'A':
            fa_transcript = fa_transcript + 'U'
        elif fa[index] == 'T':
            fa_transcript = fa_transcript + 'A'
        elif fa[index] == 'C':
            fa_transcript = fa_transcript + 'G'
        else:
            fa_transcript = fa_transcript +'C'
    fa_rc = ''
    for i in range(len(fa_transcript)):
        index = -(i+1)
        if fa_transcript[index] == 'A':
            fa_rc = fa_rc + 'U'
        elif fa_transcript[index] == 'U':
            fa_rc = fa_rc + 'A'
        elif fa_transcript[index] == 'C':
            fa_rc = fa_rc + 'G'
        else:
            fa_rc = fa_rc +'C'
    return fa_transcript, fa_rc

def find_all(s,substring):
    '''
    this function is for find all substrings in one string.
    It returns the index(es) of the start of all substring(s).
    '''
    index_list = []
    index = s.find(substring)
    while index != -1: #find() returns -1 if there is no match.
        index_list.append(index)
        index = s.find(substring, index+1)
    #mimic the return rule of find()
    if len(index_list) > 0:
        return index_list
    else:
        return -1

def orf(mrna):
    #finding = find_all(mrna, 'AUG')
    #print(finding)
    start_codon = 'AUG'
    stop_codon = ['UAA', 'UAG', 'UGA']
    i, j = 0,0
    out = []
    while i <= len(mrna)-2:
        if mrna[i:i+3] == start_codon:
            j=i
            sequence=''
            while i<= len(mrna) -2:
                if mrna[i:i+3] in stop_codon:
                    out.append(sequence)
                    break
                sequence = sequence + mrna[i:i+3]
                i = i+3
        i = j+1
        j = j+1
    #print(out)
    return out

def translate(rnaseq):
    codon_table = { 'UUU': 'F', 'CUU': 'L', 'AUU': 'I', 'GUU': 'V', \
                    'UUC': 'F', 'CUC': 'L', 'AUC': 'I', 'GUC': 'V', \
                    'UUA': 'L', 'CUA': 'L', 'AUA': 'I', 'GUA': 'V', \
                    'UUG': 'L', 'CUG': 'L', 'AUG': 'M', 'GUG': 'V', \
                    'UCU': 'S', 'CCU': 'P', 'ACU': 'T', 'GCU': 'A', \
                    'UCC': 'S', 'CCC': 'P', 'ACC': 'T', 'GCC': 'A', \
                    'UCA': 'S', 'CCA': 'P', 'ACA': 'T', 'GCA': 'A', \
                    'UCG': 'S', 'CCG': 'P', 'ACG': 'T', 'GCG': 'A', \
                    'UAU': 'Y', 'CAU': 'H', 'AAU': 'N', 'GAU': 'D', \
                    'UAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D', \
                    'UAA': 'Stop', 'CAA': 'Q', 'AAA': 'K', 'GAA': 'E', \
                    'UAG': 'Stop', 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E', \
                    'UGU': 'C', 'CGU': 'R', 'AGU': 'S', 'GGU': 'G', \
                    'UGC': 'C', 'CGC': 'R', 'AGC': 'S', 'GGC': 'G', \
                    'UGA': 'Stop', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G', \
                    'UGG': 'W', 'CGG': 'R', 'AGG': 'R', 'GGG': 'G'}
    length = len(rnaseq)
    proseq = []
    for i in range(0,length,3):
        triplet = rnaseq[i:i+3]
        if codon_table[str(triplet)] != 'Stop':
            proseq.append(codon_table[str(triplet)])
        else:
            break
    proseq = ''.join(proseq)
    return proseq


# dna = 'TATACATCACTCCAGGCATCAGAAAATCATGAGAAAGTCTGTGCGCGTAGCGAGAAGGTAGGCTCATTTGTTACCCTTGGACAACTACTGCCGCGTCTGGGCCTCCAAATCGGCTGGTCTTTTTCAGCTCCGTCTTAGGTATCGCGAAATGGACGGGAGGACCATAACTTACCTCCTCTTCTTTTGGCAGTCAGGCTATGACCACGTTTTGTCGGTTACAGATCACCTACCGCGGCGTAACACTGGTGCATATAGCTTGGTTGGGTTGCCTCTCCGCCTTCTCTGACTGGCGAGTGTACGGTAGGAACGCCGGTTCAATTGCATGCTCTGACCTTCTCAGGTAGAATTTCCAGACGAGTTGACAGACTCATCGTTACGCGGGCGGCGGTTCCAAAGCTCCTTACTAGAGATAGACAAGCGCCTAAATGGTTGCTTCCCGAGACGTTCATTAGCTAATGAACGTCTCGGGAAGCAACCATCATATCGATCCCGTGAATCCCTGCCCGTATGCCCCACAGGATAAGGATACACCAGTGACTGAACCTCTGCAATAGTCAGAGATCAGGGTGCTCTTTCATAGCTAATAGCTAGGCCGCGTACTTTAAGTTGTAACACTAACTGCTATGTGGTGAGCTTGAACGCGCGAAGCTGCCCCACAAGATGAAATATGGCCTTCGGAAAGATCACATTCTTGACCTCTGGGGTGTCACTTAAAATTGGCGAAGGTCGGAAAACTCTTTCTATTGCCCGCAAGGCTAAATGGTTCCAACCCCGATGTGTATTTCTCAAACTTTTCAGGTTTTTCTGAGTTACGAACAAGGGCTCGAGCGTGGGAATAGTTTAAATGAACTGTAGATTGAAGTATCGCAAGGAGGAAGTATTCTCTATCAGACGCTTGGTCACG'
dna = 'GGGTAGTGCGCCTTCTGTCTTGTAGGCTAACGACTAGTAAGAACGTTACCCTCATGGATTGCCATTTTGAGAACCCGAAGTTTGCAAAGCCACACCTTCTAGCTTGGCTATGTGTATCCTGACACCGCTCTCTACCTCAACTCTACCTCGACTAAGAAGCACGATGACCACGAGCCCCTTAGCATCCCGTCAGTTTGATCAGCTTCATACATATTAGTGTTGGGATACTACACTTCGTGTCAAGTCCGATTACTCAGAACACCACAAGTCCTGGAGCAACTGGACCCGCCGGTTAAGCTGTTATAAGATGACAGTGAGCAATGCTGGCCGCAAGTTCTCATACCGTCCCTGATATCTTAAGCACGGCCTTGGGGATCTCCGTTAATGTGCTAGCGACCGACTCGACGTCAAGAGAGACTTGGCTGGGGTCTCCCACACAGCTTTATCTCAAGACTATCACCAGATAATGTTGTCACACCCATGGTAGCTACCATGGGTGTGACAACATCTTTACGATAGAATTCGAGGAGCCGCGTGCAAAGTTTCAGGCCCGTTAGTGAGCGTCTGCTATGACCTGTAGAACGTAACGAACATATATCGGTCACAAGCCAGTCAGAAAGTGACACCTATGGTCTTGGAACTACTAACATACGGCGCGGGCGTGCGAAGTTAAGTGTCAAGCGGCCGTGTCCTTGTTAGGCGTTCTCGACCCCCTAGCCACCCGAGTAGCCTTGTACTCTAGTCAATGAGTCTGTTTAGCAGTCCACGTCGGGGCGAGACTGTGCCACCACTAATTTGACGAGAGAGTACCAAACTTGAGTTGATTTGGCTTTCGTAATATACACTCTGGTCTATGTCGCGCAGAATCCACGAGGGTAGAGCCGGTCTTCTCCCGGCTATTGATCACACAGTCTGTATCATAGGTCGAAATGTGGAGTACACGTCTGCATCATTGCCAACCATATCCCCCTGCC'
mrna1, mrna2 = rev_comp(dna)
#print(mrna1, mrna2)
orf_list1=orf(mrna1)
orf_list2=orf(mrna2)
orf_list = orf_list1
for i in orf_list2:
    if i not in orf_list:
        orf_list.append(i)
#print(orf_list)
for i in orf_list:
    print(translate(i))