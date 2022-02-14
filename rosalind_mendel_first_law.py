def mendel_first_law(k,m,n):
    pop = k + m + n
    prob = (4*(k*(k-1)+2*k*m+2*k*n+m*n)+3*m*(m-1))/(4*pop*(pop-1))
    print(prob)

mendel_first_law(15,18,22)