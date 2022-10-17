def evenN(N):
    if N>0:
        evenN(N-1)
        print(N*2,end=' ')
