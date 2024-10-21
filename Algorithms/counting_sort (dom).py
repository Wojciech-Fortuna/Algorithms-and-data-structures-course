def Counting_sort (A):
    n=len(A)
    k=A[0]
    for i in range (1,n):
        if k<A[i]:
            k=A[i]
    
    C=[0]*(k+1)
    B=[0]*n
    for i in range (n):
        C[A[i]]+=1
    for i in range (1,k+1):
        C[i]=C[i]+C[i-1]
    for i in range (n-1,-1,-1):
        B[C[A[i]]-1]=A[i]
        C[A[i]]-=1
    for i in range (n):
        A[i]=B[i]



n=int(input("Podaj wielkosc tablicy: "))
A=[0 for _ in range (n)]
for i in range (0,n):
    A[i]=int(input("Podaj "+str(i)+" liczbe: "))

Counting_sort(A)
print (A)

