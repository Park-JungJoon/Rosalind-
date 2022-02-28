import re
def translate(a):
    RNA_seq = a
    codon_table ={'TTT': 'F', 'TTC': 'F', 'TTA': 'L', 'TTG': 'L', 'TCT': 'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S', 'TAT': 'Y', 'TAC': 'Y', 'TAA': '*', 'TAG': '*', 'TGT': 'C', 'TGC': 'C', 'TGA': '*', 'TGG': 'W', 'CTT': 'L', 'CTC': 'L', 'CTA': 'L', 'CTG': 'L', 'CCT': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P', 'CAT': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q', 'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R', 'ATT': 'I', 'ATC': 'I', 'ATA': 'I', 'ATG': 'M', 'ACT': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T', 'AAT': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K', 'AGT': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R', 'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V', 'GCT': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A', 'GAT': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E', 'GGT': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'}
    start_codon = RNA_seq.find('ATG')
    AA_seq = []
    i = start_codon
    while i < len(RNA_seq)-2:
        codon = RNA_seq[i:i+3]
        AA = codon_table[codon]
        i+=3
        AA_seq.append(AA)
    return ''.join(AA_seq)

def ORF(a):
    result = re.findall(r'(?=(M[A-Z]*\*))',a)
    return(result)

def complementary_dna(dna_seq):
    replace_bases = {"A":"T","T":"A","G":"C","C":"G"}
    return ''.join([replace_bases[base] for base in reversed(dna_seq)])
    
Answers = []
given_seq = 'GTTGCTGACCATTCCGCAGTGAGGGAGCCGCCTGCCAATAGTGTCAAATCTCCGCACTAATTTAAAGTAAGTCCGTCACCAACTCGTTCGTGAAAGGTTGAAAACTTGAAAACCCGCGAAACGATTCCTGAGTATCAAGTCATTGCTTAGACTGCAGCACTGACTAGAGGTGGACGCCCTTCACTTGATGTCTCCCGCCTATGCGTTTTAGATCTAAATTCGGGACCGTTTGAACAAAACTCTGCTTCGTCTCTATATAACGAAAGACACGACTAGCATGGTCGACCCTTGACAGTCACTAAAAGATCAGTATCATTAGAGATTCCGAGGTCGCCTAAACGTACACATAAAAACCAGCGCGCCTGCTGGGAACTCACCTAGCCAAGTGCGGCAAATCCCCGCGCAAACCTCCCTATGCTGGAGTGAACATGTGACTAGCTAGTCACATGTTCACTCCAGCATTAACGACGCACAGGCTGTTGTTGCTGTACGCCATCGGACTGCGTGGGACGTAAAACGCACTAAACAGAGGCAGCTCATGTAGATATGCATGATGCACGGCCACAATTGATACACTATAGTGTCCAAGCTGAAAAAGGAACCAGCAAGCACACAACTCGTGCAGTACCCTAAAAGGGTTCCTGCGGCCGTCAATCGTACGGTATCGCACCGGCGAGCGTTCACGGTCCTGTGCGGCCGTTCTACTCACTCACACCCAGCTCGTTACGATTTTTGAACCAGGAACAATCAACTTTTAGATCACACCCCCACTGGACGTGATGACAATGTTGTCTACCCCGAAAGGTTATAGTAAACTCGGGTCGCTAGGTTTCCTCATGTTCCAACGTCCAGCGAAGCCTAATCTTCTGAACTTGC'
compliment_seq =complementary_dna(given_seq)
DNA_set = [given_seq, compliment_seq]
for DNA in DNA_set:
    Start_codon_site = []
    re_iter = re.finditer('ATG', DNA)
    for span_start_site in re_iter:
        Start_codon_site.append(span_start_site.start())

    Raw_ORF_data = []
    for i in Start_codon_site:
        Raw_ORF_data.append(translate(DNA[i:]))

    for Raw_AA_seq in Raw_ORF_data:
        Answers.extend(ORF(Raw_AA_seq))

Answers_nonoverlapping = set(Answers)

for non_overlapping_answer in Answers_nonoverlapping:
    print(non_overlapping_answer[:-1])