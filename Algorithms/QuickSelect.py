def partition (T,l,r):
    i=l
    j=l
    while j<r:
        if T[j]<=T[r]:
            T[i],T[j]=T[j],T[i]
            i+=1
            j+=1
        else:
            j+=1
    T[r],T[i]=T[i],T[r]
    return i


def QuickSelect (T,l,r,k):
    pivot_idx=partition(T,l,r)
    if pivot_idx-l+1==k:
        return T[pivot_idx]
    elif pivot_idx-l+1>k:
        return QuickSelect(T,l,pivot_idx-1,k)
    else:
        return QuickSelect(T,pivot_idx+1,r,k-(pivot_idx-l+1))





n=int(input("Podaj wielkosc tablicy: "))
S=[0 for _ in range (n)]
for i in range (0,n):
    S[i]=int(input("Podaj "+str(i)+" liczbe: "))

k=int(input("Podaj k-najmniejsza liczbe: "))
n=len(S)
result=QuickSelect(S,0,n-1,k)
print (result)
