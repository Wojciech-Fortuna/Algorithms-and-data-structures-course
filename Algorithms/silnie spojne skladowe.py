
def Silnie_spojne_skladowe(G):
    n=len(G)
    G2=[[] for _ in range (n)] 
    visited=[False for _ in range (n)]
    visited_reversed=[True for _ in range (n)]
    processed_list=[False for _ in range (n)]
    processed_reversed_list=[False for _ in range (n)]
    result=[]

    for k in range (0,n):
        if visited[k]==False:
            stack=[k]
            DFS_visit=[]
            while len(stack)!=0:
                checked=stack[len(stack)-1]
                if processed_list[checked]==True:
                    stack.pop()
                else:
                    visited[checked]=True
                    visited_reversed[checked]=False
                    processed=True
                    m=len(G[checked])
                    for i in range (0,m):
                        new_to_add=G[checked][i]
                        if visited[new_to_add]==False:
                            stack.append(new_to_add)
                            processed=False
                    if processed==True:
                        stack.pop()
                        processed_list[checked]=True
                        DFS_visit.append(checked)
                        m=len(G[checked])
                        for i in range (0,m):
                            G2[G[checked][i]].append(checked)

            highest_rank=len(DFS_visit)
            while highest_rank!=0:
                highest_rank-=1
                if visited_reversed[DFS_visit[highest_rank]]==False:
                    stack=[DFS_visit[highest_rank]]
                    new_result=[]
                    while len(stack)!=0:
                        checked=stack[len(stack)-1]
                        if processed_reversed_list[checked]==True:
                            stack.pop()
                        else:
                            visited_reversed[checked]=True
                            processed_reversed=True
                            m=len(G2[checked])
                            for i in range (0,m):
                                new_to_add=G2[checked][i]
                                if visited_reversed[new_to_add]==False:
                                    stack.append(new_to_add)
                                    processed_reversed=False
                            if processed_reversed==True:
                                stack.pop()
                                processed_reversed_list[checked]=True
                                new_result.append(checked)
                    result.append(new_result)

    T_order=[0 for _ in range (n)]
    for i in range (0,len(result)):
        for j in range (0,len(result[i])):
            T_order[result[i][j]]=i

    result_order=[[] for _ in range (len(result))]
    for i in range (0,n):
        result_order[T_order[i]].append(i)

    return result_order



n=int(input("Podaj liczbe wierzcholkow w grafie: "))
print ("")
G=[[] for _ in range (n)]
for i in range (n):
    m=int(input("Podaj liczbe sasiadow "+str(i)+" wierzcholka: "))
    for j in range (m):
        nazwa=int(input("Podaj nazwe "+str(j)+" sasiada "+str(i)+" wierzcholka: "))
        G[i].append(nazwa)
    print ("")

result=Silnie_spojne_skladowe(G)
print (result)
