seq ='AAAACCCGGT'
seq.replace('A','X')
seq.replace('T','A')
seq.replace('C','Y')
seq.replace('G','C')
seq.replace('X','C')
seq.replace('Y','G')
answer = ''.join[list(seq).reverse]
print((answer))