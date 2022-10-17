def revernum(N):
    if N//10==0:
        print(N)
    else:
        print(N%10,end='')
        revernum(N//10)
