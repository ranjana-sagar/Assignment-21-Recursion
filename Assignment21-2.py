def reverseN(N):
    if N>0:
        print(N,end=' ')
        reverseN(N-1)

reverseN(50)        
