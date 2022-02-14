a='GATATACA'
b='TAGACCA'
c='ATACA'
def finding_multi_motif(x, y, z):
    max_motif = ''
    for j in range (2,len(x)):
        while j < len(x):
            for i in range(0, len(x)):
                if x[i:i+j] in y and z:
                    motif = a[i: i+j]
                    if len(max_motif) > len(motif):
                        max_motif = motif
                        print(max_motif)

a = 'ATTGC'
b = 'ATATT'
C = 'GCATT'
finding_multi_motif(a,b,c)


