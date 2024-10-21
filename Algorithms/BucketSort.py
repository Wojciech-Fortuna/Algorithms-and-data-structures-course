
def CountingSort(A,divider):
    n=len(A)
    k=A[0]//(n**divider)
    for i in range (1,n):
        if k<A[i]//(n**divider):
            k=A[i]//(n**divider)

    C=[0]*(k+1)
    B=[0]*n
    for i in range (n):
        C[A[i]//(n**divider)]+=1
    for i in range (1,k+1):
        C[i]=C[i]+C[i-1]
    for i in range (n-1,-1,-1):
        B[C[A[i]//(n**divider)]-1]=A[i]
        C[A[i]//(n**divider)]-=1
    for i in range (n):
        A[i]=B[i]


def BucketSort(A):
    #elementy od (0,(n^2)-1)
    #zlozonosc tego przypadku O(n)

    n=len(A)
    CountingSort(A,1)
    begin=0
    end=0
    F=[]
    while end<n:
        if A[begin]//n!=A[end]//n:
            for i in range (begin,end):
                F.append(A[i])
            CountingSort(F,0)
            for i in range (begin,end):
                A[i]=F[i-begin]
            begin=end
            F.clear()
        else:
            end+=1
    return A


n=int(input("Podaj rozmiar tablicy: "))
A=[0 for _ in range (n)]
for i in range (n):
    A[i]=int(input("Podaj "+str(i)+" element: "))
print(BucketSort(A))
        
    
