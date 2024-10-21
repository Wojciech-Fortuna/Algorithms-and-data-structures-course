
def BlackForest(T):
    n=len(T)
    F=[0 for _ in range (n)]
    F[0]=T[0]
    if n==1: return F[0]
    F[1]=max(T[0],T[1])
    if n==2: return F[1]

    for i in range (2,n):
        F[i]=max(F[i-1],F[i-2]+T[i])
    return F[n-1]



n=int(input("Podaj rozmiar tablicy: "))
T=[0 for _ in range (n)]
for i in range (n):
    T[i]=int(input("Podaj zysk z "+str(i)+" drzewa: "))
print (BlackForest(T))
