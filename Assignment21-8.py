def cuben(N):
    if N>0:
        cuben(N-1)
        print(N**3,end=' ')
