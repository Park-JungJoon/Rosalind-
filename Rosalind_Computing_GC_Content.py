def GCcontent(a):
    result = 0
    if 'G'or 'C' in a:
        result=result+1
    elif 'A'or 'T'in a:
        result=result
    else:
        pass
    print(result / len(a) * 100)
    
a = ('A','T','G','C')
GCcontent(a)

