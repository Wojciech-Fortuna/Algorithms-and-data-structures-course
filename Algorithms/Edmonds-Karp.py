from collections import deque

def Edmonds_Karp(G,s,t):
    n=len(G)
    T=[[] for _ in range (n)]
    edges_table=[[[0,0] for _ in range (n)] for _ in range (n)]

    for i in range (0,n):
        for j in range (0,len(G[i])):
            new_index=G[i][j][0]
            T[i].append(new_index)
            edges_table[i][new_index][1]=G[i][j][1]
            T[new_index].append(i)

    result=0
    end_searching=False

    while end_searching==False:
        visited=[False for _ in range (n)]
        parents=[-1 for _ in range (n)]
        queue=deque()
        queue.append(s)
        visited[s]=True
        found=False
        while len(queue)!=0 and found==False:
            checked=queue.popleft()
            for i in range (0,len(T[checked])):
                new_name=T[checked][i]
                if edges_table[checked][new_name][1]-edges_table[checked][new_name][0]>0:
                    if visited[new_name]==False:
                        visited[new_name]=True
                        queue.append(new_name)
                        parents[new_name]=checked
                    if new_name==t:
                        found=True
                        break



        if len(queue)!=0:
            botomneck=float('inf')
            travel=t
            while travel!=s:
                checked_value=edges_table[parents[travel]][travel][1]-edges_table[parents[travel]][travel][0]
                if checked_value<botomneck:
                    botomneck=checked_value
                travel=parents[travel]
            result+=botomneck

            travel=t
            while travel!=s:
                edges_table[parents[travel]][travel][0]+=botomneck
                edges_table[travel][parents[travel]][0]-=botomneck
                travel=parents[travel]

        else:
            end_searching=True

    
    return result



n=int(input("Podaj liczbe wierzcholkow w grafie: "))
print ("")
G=[[] for _ in range (n)]
for i in range (n):
    m=int(input("Podaj liczbe sasiadow "+str(i)+" wierzcholka: "))
    for j in range (m):
        name=int(input("Podaj nazwe "+str(j)+" sasiada "+str(i)+" wierzcholka: "))
        flow=int(input("Podaj wielkosc przeplywu miedzy tymi wierzchokami: "))
        G[i].append([name,flow])
    print ("")

start=int(input("Podaj nazwe wierzcholka startowego: "))
end=int(input("Podaj nazwe wierzcholka koncowego: "))

result=Edmonds_Karp(G,start,end)
print (result)

