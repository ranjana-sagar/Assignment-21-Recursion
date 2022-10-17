def oddn(N):
    if N>0:
        oddn(N-1)
        print(N*2-1,end=' ')
