def MortalFibonacci(n, m):
    rabbit = [1, 1]
    for i in range(2, n):
        total = rabbit[i - 1] + rabbit[i - 2]
        if i == m:
            total = total - 1
        if i > m:
            total = total - rabbit[i - m - 1]
        rabbit.append(total)
    return rabbit[-1]

print(MortalFibonacci(90,16))