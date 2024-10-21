
def mosty(G):
    stack=[0]
    n=len(G)
    visited=[False for _ in range (n)]
    list_processed=[False for _ in range (n)]
    low=[-1 for _ in range (n)]
    parent=[-1 for _ in range (n)]
    time_visit=[0 for _ in range (n)]
    bridges=[]
    time=0

    while len(stack)!=0:
        checked=stack[len(stack)-1]
        if list_processed[checked]==False:
            if visited[checked]==False:
                time+=1
                time_visit[checked]=time
            current_low=time
            visited[checked]=True
            processed=True
            m=len(G[checked])
            for i in range (0,m):
                new_to_add=G[checked][i]
                if visited[new_to_add]==False:
                    stack.append(new_to_add)
                    parent[new_to_add]=checked
                    processed=False
                else:
                    if parent[checked]!=new_to_add:
                        if low[new_to_add]<current_low:
                            current_low=low[new_to_add]
            low[checked]=current_low
            if processed==True:
                stack.pop()
                list_processed[checked]=True
                if time_visit[checked]==low[checked] and parent[checked]!=-1:
                    bridges.append([checked,parent[checked]])
        else:
            stack.pop()

    return bridges






n=int(input("Podaj liczbe wierzcholkow w grafie: "))
print ("")
G=[[] for _ in range (n)]
for i in range (n):
    m=int(input("Podaj liczbe sasiadow "+str(i)+" wierzcholka: "))
    for j in range (m):
        nazwa=int(input("Podaj nazwe "+str(j)+" sasiada "+str(i)+" wierzcholka: "))
        G[i].append(nazwa)
    print ("")

result=mosty(G)
print (result)
