
def Sort (G,start):
    stack=[start]
    n=len(G)
    visited=[False for _ in range (n)]
    proceeded_list=[False for _ in range (n)]
    topological_list=[]

    while len(stack)!=0:
        checked=stack[len(stack)-1]
        if proceeded_list[checked]==True:
            stack.pop()
        else:
            visited[checked]=True
            m=len(G[checked])
            proceeded=True
            for i in range (0,m):
                new_to_add=G[checked][i]
                if visited[new_to_add]==False:
                    stack.append(new_to_add)
                    proceeded=False
            if proceeded==True:
                stack.pop()
                proceeded_list[checked]=True
                topological_list.append(checked)

    topological_list.reverse()
    return topological_list







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

result=Sort(G,start)
print (result)
