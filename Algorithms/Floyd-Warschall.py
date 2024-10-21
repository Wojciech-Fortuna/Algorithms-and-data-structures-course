import copy

def Floyd_Warschall(T):
    G=copy.deepcopy(T)
    n=len(G)
    for i in range (0,n):
        G[i][i]=0

    for k in range (0,n):
        for i in range (0,n):
            for j in range (0,n):
                if G[i][j]>G[i][k]+G[k][j]:
                    G[i][j]=G[i][k]+G[k][j]


    for checked in range (0,n):
        priority_old=G[0][checked]
        for i in range (0,n):
            if i!=checked and T[checked][i]!=float('inf'):
                priority_new=G[0][i]
                distance=T[checked][i]
                if priority_new!=float('inf') and priority_new>priority_old+distance:
                    return None

    return G












n=int(input("Podaj liczbe wierzcholkow w grafie: "))
print ("")
T=[[float('inf') for _ in range (n)] for _ in range (n)]
for i in range (n):
    m=int(input("Podaj liczbe sasiadow "+str(i)+" wierzcholka: "))
    for j in range (m):
        nazwa=int(input("Podaj nazwe "+str(j)+" sasiada "+str(i)+" wierzcholka: "))
        odleglosc=int(input("Podaj odleglosc miedzy tymi wierzchokami: "))
        T[i][nazwa]=odleglosc
    print ("")

result=Floyd_Warschall(T)
print (result)
        
