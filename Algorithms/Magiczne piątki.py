
def partition (T,pivot_idx):
    n=len(T)
    T[pivot_idx],T[n-1]=T[n-1],T[pivot_idx]
    i=0
    j=0
    while j<len(T)-1:
        if T[j]<=T[n-1]:
            T[i],T[j]=T[j],T[i]
            i+=1
            j+=1
        else:
            j+=1
    T[n-1],T[i]=T[i],T[n-1]
    return i


def find_pivot(F,idx):
    if len(F)==1: return idx[0]
    Medians=[]
    new_idx=[]
    l=0
    r=min(4,len(F)-1)
    while l<len(F):
        for i in range (l,r+1):
            checked=F[i]
            checked_idx=idx[i]
            j=i-1
            while j>=l and F[j]>checked:
                F[j+1]=F[j]
                idx[j+1]=idx[j]
                j-=1
            F[j+1]=checked
            idx[j+1]=checked_idx
        Medians.append(F[l+((r-l)//2)])
        new_idx.append(idx[l+((r-l)//2)])
        l+=5
        r=min(r+5,len(F)-1)
    return find_pivot(Medians,new_idx)


def Median_of_Medians(T,k):
    F=[T[i] for i in range (len(T))]
    idx=[i for i in range (len(T))]
    pivot_idx=find_pivot(F,idx)
    pivot_idx=partition(T,pivot_idx)
    if pivot_idx+1==k:
        return T[pivot_idx]
    elif pivot_idx+1>k:
        return Median_of_Medians(T[:pivot_idx],k)
    else:
        return Median_of_Medians(T[(pivot_idx+1):],k-(pivot_idx+1))



n=int(input("Podaj wielkosc tablicy: "))
S=[0 for _ in range (n)]
for i in range (0,n):
    S[i]=int(input("Podaj "+str(i)+" liczbe: "))
T=S.copy()
A=S.copy()
k=int(input("Podaj k-najmniejsza liczbe: "))
n=len(S)
result=Median_of_Medians(S,k)
print (result)
