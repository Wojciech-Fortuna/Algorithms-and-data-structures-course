def MergeSort (T,Perm):
    if len(T)>1:
        mid=len(T)//2
        L=T[:mid]
        L_Perm=Perm[:mid]
        R=T[mid:]
        R_Perm=Perm[mid:]
        MergeSort(L,L_Perm)
        MergeSort(R,R_Perm)
        i=j=k=0

        while i<len(L) and j<len(R):
            if L[i]>=R[j]:
                T[k]=L[i]
                Perm[k]=L_Perm[i]
                i+=1
            else:
                T[k]=R[j]
                Perm[k]=R_Perm[j]
                j+=1
            k+=1

        while i<len(L):
            T[k]=L[i]
            Perm[k]=L_Perm[i]
            i+=1
            k+=1

        while j<len(R):
            T[k]=R[j]
            Perm[k]=R_Perm[j]
            j+=1
            k+=1


def Trailer (T,K):
    n=len(T)
    Names=[0 for _ in range (n)]
    for i in range (n):
        Names[i]=i
    MergeSort(T,Names)

    i=0
    taken=0
    Result=[]
    while i<n and taken<K:
        if T[i]+taken<=K:
            taken+=T[i]
            Result.append(Names[i])
        i+=1

    Result.sort()
    return Result


n=int(input("Podaj rozmiar tablicy: "))
T=[0 for _ in range (n)]
for i in range (n):
    T[i]=int(input("Podaj wage "+str(i)+" ladunku: "))
K=int(input("Podaj pojemnosc przyczepy: "))
print (Trailer(T,K))
