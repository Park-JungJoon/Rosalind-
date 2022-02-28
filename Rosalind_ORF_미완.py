import re
given_seq = 'AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG'
#reversed만 했지, complementary를 고려하지 않아서 오류가 났다.
def complementary_dna(dna_seq):
    replace_bases = {"A":"T","T":"A","G":"C","C":"G"}
    return ''.join([replace_bases[base] for base in reversed(dna_seq)])
#단순하게 전체 시퀀스의 1번, 2번 , 3번에서 시작하는 것으로 짰는데, 시작 코돈의 위치에서부터 한개씩 밀려야 프레임이 완성된다. NNNATG형식의 경우에, 2번 염기부터 시작한다고 해서 단백질 번역에 달라지는 점이 없고, ATG에서 A를 떼고 T부터 시작하는 방식으로 바꿔야했다.
Frame_changing_site = given_seq.find('ATG')
Reverse_Frame_changing_site = complementary_dna(given_seq).find('ATG')

DNA1 = given_seq
DNA2 = given_seq[Frame_changing_site+1:]
DNA3 = given_seq[Frame_changing_site+2:]
DNA4 = complementary_dna(given_seq)
DNA5 = complementary_dna(given_seq)[Reverse_Frame_changing_site+1:]
DNA6 = complementary_dna(given_seq)[Reverse_Frame_changing_site+2:]
#DNA를 6개 지정하고 translate, ORF 함수에 돌려야했기 때문에 리스트로 만들어서 포문을 돌리려고한다. 
Frame_list = [DNA1, DNA2, DNA3, DNA4, DNA5, DNA6]
#일단 스탑코돈을 *으로 번역한 다음, M에서 시작해서 *로 끝나는 것으로 고려를 하여, 스탑코돈에 break을 넣지 않았다.
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
#re 정규표현식에 대해 더 공부해야될 것 같다. 
def ORF(a):
    result = re.findall(r'(?=(M[A-Z]*\*))',a)
    return(result)

ORF_list = []
#extend 함수를 썼을 때, 리스트안에 리스트를 넣으면, 들어가는 리스트의 대괄호를 무시하고 내용물만 넣어주는 기능이 있다. append를 쓸 경우 [[1,2]]형식이 된다.
for DNA_frame in Frame_list:
    Protein_Frame = translate(DNA_frame)
    ORF_result = ORF(Protein_Frame)
    ORF_list.extend(ORF_result)
#ORF가 M과 같이 짧을 경우, 겹치는 ORF가 있기 때문에, set을 통해서 중복을 없앤다.
ORF_nonoverlapping = set(ORF_list)
#stop codon은 번역되지 않으므로 결과물의 맨 뒤에 하나를 무시하고 출력했다.
for ORF_answer in ORF_nonoverlapping:
    print(ORF_answer[:-1])

########위의 경우 NNNNATGNNATG 꼴일 때, 3개씩 잘라 읽다가 ATG가 나오면 번역을 하고, 그 이후에 나오는 ATG에 대해서는 무시해도 된다를 코딩해야한다. 여기서 이 방법 기각