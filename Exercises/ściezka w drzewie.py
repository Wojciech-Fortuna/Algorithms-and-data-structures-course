from collections import deque

def BFS (G,start):
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

    return distance
    
def Path(T,values):
    n=len(T)
    F=[0 for _ in range (n)]
    result_arr=[0 for _ in range (n)]
    distance=BFS(T,0)
    max_layer=max(distance)
    layer=[[] for _ in range (max_layer+1)]
    for i in range (n):
        layer[distance[i]].append(i)

    for i in range (max_layer,-1,-1):
        for j in range (len(layer[i])):
            checked=layer[i][j]
            max_val_F=values[checked]
            max_val_r=values[checked]
            for k in range (len(T[checked])):
                if distance[T[checked][k]]>distance[checked]:
                    max_val_r=max(max_val_r,max_val_F+F[T[checked][k]])
                    max_val_F=max(max_val_F,F[T[checked][k]]+values[checked])
            F[checked]=max_val_F
            result_arr[checked]=max_val_r

    return max(result_arr)



n=int(input("Podaj liczbe wierzcholkow w grafie: "))
print ("")
T=[[] for _ in range (n)]
values=[0 for _ in range (n)]
for i in range (n):
    values[i]=int(input("Podaj wartosc dla "+str(i)+" wierzcholka: "))
    m=int(input("Podaj liczbe sasiadow "+str(i)+" wierzcholka: "))
    for j in range (m):
        T[i].append(int(input("Podaj nazwe "+str(j)+" sasiada "+str(i)+" wierzcholka: ")))
    print ("")
print (Path(T,values))
                
                
    
