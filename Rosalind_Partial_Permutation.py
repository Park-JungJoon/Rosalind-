def partial_Permutation(a,b):
    result = a
    for i in range (1,b):
        result *= (a-i)
        print (result)