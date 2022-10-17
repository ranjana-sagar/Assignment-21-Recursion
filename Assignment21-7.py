def squaren(N):
    if N>0:
        squaren(N-1)
        print(N*N,end=' ')
