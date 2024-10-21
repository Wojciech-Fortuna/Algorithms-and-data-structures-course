
def MergeSort (T):
    if len(T)>1:
        mid=len(T)//2
        L=T[:mid]
        R=T[mid:]
        MergeSort(L)
        MergeSort(R)
        i=j=k=0

        while i<len(L) and j<len(R):
            if L[i][1]<=R[j][1]:
                T[k]=tuple(L[i])
                i+=1
            else:
                T[k]=tuple(R[j])
                j+=1
            k+=1

        while i<len(L):
            T[k]=tuple(L[i])
            i+=1
            k+=1

        while j<len(R):
            T[k]=tuple(R[j])
            j+=1
            k+=1



def Tasks (T):
    MergeSort(T)
    Result=[]
    last=-float('inf')
    for i in range (n):
        if T[i][0]>=last:
            Result.append(i)
            last=T[i][1]
    return Result






n=int(input("Podaj liczbe zadan: "))
T=[]
for i in range (n):
    start=int(input("Podaj poczatek "+str(i)+" pierwszego zadania: "))
    stop=int(input("Podaj koniec "+str(i)+" pierwszego zadania: "))
    T.append((start,stop))
Result=Tasks(T)
for i in range (len(Result)):
    print (str(Result[i])+"   "+str(T[Result[i]]))
