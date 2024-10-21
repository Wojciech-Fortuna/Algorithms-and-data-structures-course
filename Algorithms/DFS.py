
def DFS (G,start,end):
    stack=[start]
    n=len(G)
    visited=[False for _ in range (n)]

    while len(stack)!=0:
        checked=stack[len(stack)-1]
        stack.pop()
        if visited[checked]==False:
            visited[checked]=True
            m=len(G[checked])
            for i in range (0,m):
                new_to_add=G[checked][i]
                if visited[new_to_add]==False:
                    stack.append(new_to_add)

    if visited[end]==True:
        return True
    else:
        return False





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

result=DFS(G,start,end)
print (result)
