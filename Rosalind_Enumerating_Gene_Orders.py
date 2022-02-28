import itertools

n = '1234567'
a = [' '.join(i) for i in itertools.permutations(n, 7)]
print(a)
b = '\n'.join(a)
print(len(b))
print(b)

# 고찰할 점 : itertools를 이용해서 1부터 7의 배열을 했을때 ['a1', 'a2', 'a3'식으로 나오게 되는데, a1안에 띄어쓰기를 넣어주는 것은 line 4에서 행함.]\n 이후 a1과 a2사이의 \n은 b에서 행함. 보군이한테 물어봤음.