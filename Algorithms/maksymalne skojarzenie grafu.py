
def MaxSkojarzenie(M):
    n=len(M)
    m=0
    for i in range (0,n):
        for j in range (0,len(M[i])):
            if M[i][j]>m:
                m=M[i][j]
    m+=1
    
    T=[[] for _ in range (n+m+2)]
    edges_table=[[0 for _ in range (n+m+2)] for _ in range (n+m+2)]

    for i in range (0,n):
        for j in range (0,len(M[i])):
            new_index=M[i][j]+n
            T[i].append(new_index)
            edges_table[i][new_index]=1
            T[new_index].append(i)

    s_idx=n+m
    t_idx=n+m+1
    for i in range (0,n):
        T[s_idx].append(i)
        edges_table[s_idx][i]=1
        T[i].append(s_idx)

    for i in range (n,n+m):
        T[i].append(t_idx)
        edges_table[i][t_idx]=1
        T[t_idx].append(i)



    result=0
    end_searching=False

    while end_searching==False:
        stack=[s_idx]
        visited=[False for _ in range (n+m+2)]
        parents=[-1 for _ in range (n+m+2)]
        found=False
        while len(stack)!=0 and found==False:
            checked=stack[len(stack)-1]
            stack.pop()
            visited[checked]=True
            for i in range (0,len(T[checked])):
                new_name=T[checked][i]
                if edges_table[checked][new_name]==1:
                    if visited[new_name]==False:
                        stack.append(new_name)
                        parents[new_name]=checked
                    if new_name==t_idx:
                        found=True
                        break

        if len(stack)!=0:
            travel=t_idx
            while travel!=s_idx:
                edges_table[parents[travel]][travel]=0
                edges_table[travel][parents[travel]]=1
                travel=parents[travel]
            result+=1

        else:
            end_searching=True

    
    return result



n=int(input("Podaj liczbę pracownikow: "))
M=[[] for _ in range (n)]
for i in range (0,n):
    m=int(input("Podaj liczbę maszyn dla "+str(i)+" pracownika: "))
    for j in range (0,m):
        M[i].append(int(input("Podaj nazwe "+str(j)+" maszyny dla "+str(i)+" pracownika: ")))

result=MaxSkojarzenie(M)
print (result)

