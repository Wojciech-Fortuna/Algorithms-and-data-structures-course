from collections import deque

def BFS (G, start, end):
    V=len(G)
    visited=[False for _ in range (V)]
    distance=[0 for _ in range (V)]

    queue=deque()
    queue.append(start)
    visited[start]=True
    
    while len(queue)!=0:
        checked=queue.popleft()
        for i in range (0, len(G[checked])):
            if visited[G[checked][i]]==False:
                visited[G[checked][i]]=True
                distance[G[checked][i]]=distance[checked]+1
                queue.append(G[checked][i])

    if visited[end]==False:
        return None
    else:
        return distance[end]





n=int(input("Podaj liczbe wierzcholkow w grafie: "))
print ("")
G=[[] for _ in range (n)]
for i in range (n):
    m=int(input("Podaj liczbe sasiadow "+str(i)+" wierzcholka: "))
    for j in range (m):
        nazwa=int(input("Podaj nazwe "+str(j)+" sasiada "+str(i)+" wierzcholka: "))
        G[i].append(nazwa)
    print ("")

start=int(input("Podaj nazwe wierzcholka startowego: "))
end=int(input("Podaj nazwe wierzcholka koncowego: "))

result=BFS(G,start,end)
print (result)
