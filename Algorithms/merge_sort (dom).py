def MergeSort (T):
    if len(T)>1:
        mid=len(T)//2
        L=T[:mid]
        R=T[mid:]
        MergeSort(L)
        MergeSort(R)
        i=j=k=0

        while i<len(L) and j<len(R):
            if L[i]<=R[j]:
                T[k]=L[i]
                i+=1
            else:
                T[k]=R[j]
                j+=1
            k+=1

        while i<len(L):
            T[k]=L[i]
            i+=1
            k+=1

        while j<len(R):
            T[k]=R[j]
            j+=1
            k+=1


n=int(input("Podaj dlugosc tablicy: "))
T=[0 for _ in range (n)]
for i in range (0,n):
    T[i]=int(input("Podaj wartosc dla indeksu "+str(i)+": "))
print (T)
MergeSort (T)
print (T)
