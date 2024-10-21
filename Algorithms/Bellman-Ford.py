
def Bellman_Ford (G,start,end):
    n=len(G)
    parents=[[-1,0] for _ in range (n)]
    list_of_priorities=[float('inf') for _ in range (n)]
    list_of_priorities[start]=0
    
    for k in range (0,n-1):
        for checked in range (0,n):
            priority_old=list_of_priorities[checked]
            for i in range (0,len(G[checked])):
                priority_new=list_of_priorities[G[checked][i][0]]
                distance=G[checked][i][1]
                if priority_new==float('inf') or priority_new>priority_old+distance:
                    priority_new=priority_old+distance
                    new=G[checked][i][0]
                    list_of_priorities[new]=priority_new
                    parents[new][0]=checked
                    parents[new][1]=distance

    for checked in range (0,n):
        priority_old=list_of_priorities[checked]
        for i in range (0,len(G[checked])):
            priority_new=list_of_priorities[G[checked][i][0]]
            distance=G[checked][i][1]
            if priority_new!=float('inf') and priority_new>priority_old+distance:
                return None

    if parents[end][0]==-1:
        return None
    
    result=0
    travel=end
    while start!=travel:
        result+=parents[travel][1]
        travel=parents[travel][0]

    return result





n=int(input("Podaj liczbe wierzcholkow w grafie: "))
print ("")
G=[[] for _ in range (n)]
for i in range (n):
    m=int(input("Podaj liczbe sasiadow "+str(i)+" wierzcholka: "))
    for j in range (m):
        nazwa=int(input("Podaj nazwe "+str(j)+" sasiada "+str(i)+" wierzcholka: "))
        odleglosc=int(input("Podaj odleglosc miedzy tymi wierzchokami: "))
        G[i].append([nazwa,odleglosc])
    print ("")

start=int(input("Podaj nazwe wierzcholka startowego: "))
end=int(input("Podaj nazwe wierzcholka koncowego: "))

result=Bellman_Ford(G,start,end)
print (result)
        
