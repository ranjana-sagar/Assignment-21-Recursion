def reverodd(N):
    if N>0:
        print(N*2-1,end=' ')
        reverodd(N-1)
