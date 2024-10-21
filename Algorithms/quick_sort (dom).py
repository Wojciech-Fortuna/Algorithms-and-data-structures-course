def partition (S,p,r):
    x=S[r]
    i=p-1
    for j in range (p,r):
        if S[j]<=x:
            i+=1
            S[i],S[j]=S[j],S[i]
    S[i+1],S[r]=S[r],S[i+1]
    return i+1




def quicksort (S,p,r):
    if p<r:
        q=partition (S,p,r)
        quicksort (S,p,q-1)
        quicksort (S,q+1,r)


n=int(input("Podaj wielkosc tablicy: "))
S=[0 for _ in range (n)]
for i in range (0,n):
    S[i]=int(input("Podaj "+str(i)+" liczbe: "))

n=len(S)
quicksort(S,0,n-1)
print (S)
