
def MergeSort (T,Perm):
    if len(T)>1:
        mid=len(T)//2
        L=T[:mid]
        R=T[mid:]
        L_Perm=Perm[:mid]
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



def knupsuck (W,P,B):
    n=len(W)
    F=[0 for _ in range (n)]
    for i in range (n):
        F[i]=P[i]/W[i]
    Perm=[0 for _ in range (n)]
    for i in range (n):
        Perm[i]=i
    MergeSort(F,Perm)

    result=0    
    last_elem=False
    i=0
    while last_elem==False and i<n:
        if W[Perm[i]]<=B:
            result+=P[Perm[i]]
            B-=W[Perm[i]]
            i+=1
        else:
            last_elem=True

    if i!=n:
        result+=P[Perm[i]]*B/W[Perm[i]]
    return result
    







n=int(input("Podaj liczbe przedmiotow: "))
W=[0 for _ in range (n)]
P=[0 for _ in range (n)]
for i in range (0,n):
    W[i]=int(input("Podaj wage "+str(i)+" przedmiotu: "))
    P[i]=int(input("Podaj cene "+str(i)+" przedmiotu: "))
B=int(input("Podaj maksymalna wage plecaka: "))
print (knupsuck(W,P,B))
