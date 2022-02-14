massTableDictionary = {"A" : 71.03711, "C" : 103.00919, "D" : 115.02694, "E" : 129.04259,
                "F" : 147.06841, "G" : 57.02146, "H" : 137.05891, "I" : 113.08406,
                "K" : 128.09496, "L" : 113.08406, "M" : 131.04049, "N" : 114.04293,
                "P" : 97.05276, "Q" : 128.05858, "R" : 156.10111, "S" : 87.03203,
                "T" : 101.04768, "V" : 99.06841, "W" : 186.07931, "Y" : 163.06333}

aa_seq= ['S','K','A','D','Y','E','K']
mass = []
for aa in aa_seq:
    mass.append(massTableDictionary[aa])

print(mass)
sum(mass)
##############################################
def counting_protein_mass(a):
    aa_seq = list(a)
    mass = []
    for aa in aa_seq:
        mass.append(massTableDictionary[aa])
    return sum(mass)

###retrun을 입력하지 않아서 실행값을 못 받았음. sum(mass)라인을 def에 걸리는 ---라인이 아니라 >>>라인에 써서 오류 났었음