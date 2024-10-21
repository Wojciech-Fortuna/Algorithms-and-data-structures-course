
def Zaba(A):
    n=len(A)
    if n==1: return 0
    F=[[float('inf') for _ in range (n)] for _ in range (n)]
    for i in range (n):
        F[n-1][i]=0

    for i in range (n-2,-1,-1):
        for j in range (n):
            min_val=float('inf')
            if j+A[i]<n:
                for k in range (i+1,min(i+j+A[i]+1,n)):
                    min_val=min(min_val,F[k][min(j+A[i]+i-k,n-1)])
            F[i][j]=min_val+1

    return F[0][0]




n=int(input("Podaj rozmiar tablicy: "))
A=[0 for _ in range (n)]
for i in range (n):
    A[i]=int(input("Podaj wartosc energetyczna na "+str(i)+" polu: "))
print (Zaba(A))
