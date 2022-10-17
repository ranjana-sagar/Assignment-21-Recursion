def table(N,multi):
    if multi>0:
        table(N,multi-1)
        print(N*multi,end=' ')

N=int(input("Enter a number:"))
multi=int(input("how many multiple you want to print:"))
table(N,multi)
