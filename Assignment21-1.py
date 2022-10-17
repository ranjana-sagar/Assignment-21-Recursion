def firstN(N):
    if N>0:
        firstN(N-1)
        print(N,end=' ')

firstN(100)        
