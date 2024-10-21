from math import sqrt

def distance(elem1,elem2,T):
    a=T[elem1][0]-T[elem2][0]
    b=T[elem1][1]-T[elem2][1]
    return sqrt((a**2)+(b**2))

def Komiwojazer(T):
    n=len(T)
    if n<2: return 0
    F=[[float('inf') for _ in range (n)] for _ in range (n)]
    F[0][1]=distance(0,1,T)
    min_result=float('inf')
    for i in range (n-1):
        min_result=min(min_result,tspf(i,n-1,F,T)+distance(i,n-1,T))
    return min_result


def tspf(i,j,F,T):
    if F[i][j]!=float('inf'): return F[i][j]
    if i==j-1:
        best=float('inf')
        for k in range (j-1):
            best=min(best,tspf(k,j-1,F,T)+distance(k,j,T))
        F[j-1][j]=best
    else:
        F[i][j]=tspf(i,j-1,F,T)+distance(j-1,j,T)
    return F[i][j]





    

n=int(input("Podaj liczbe miast: "))
T=[]
for i in range (n):
    d=int(input("Podaj dlugosc geograficzna dla miasta "+str(i)+": "))
    s=int(input("Podaj szerokosc geograficzna dla miasta "+str(i)+": "))
    T.append((d,s))
print (Komiwojazer(T))
