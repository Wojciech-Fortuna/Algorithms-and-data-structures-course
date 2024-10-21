
def MergeSort (T,Perm):
    if len(T)>1:
        mid=len(T)//2
        L=T[:mid]
        L_Perm=Perm[:mid]
        R=T[mid:]
        R_Perm=Perm[mid:]
        MergeSort(L,L_Perm)
        MergeSort(R,R_Perm)
        i=j=k=0

        while i<len(L) and j<len(R):
            if L[i]<=R[j]:
                T[k]=L[i]
                Perm[k]=L_Perm[i]
                i+=1
            else:
                T[k]=R[j]
                Perm[k]=R_Perm[j]
                j+=1
            k+=1

        while i<len(L):
            T[k]=L[i]
            Perm[k]=L_Perm[i]
            i+=1
            k+=1

        while j<len(R):
            T[k]=R[j]
            Perm[k]=R_Perm[j]
            j+=1
            k+=1


def DFS (G,start,end):
    stack=[start]
    n=len(G)
    visited=[False for _ in range (n)]

    while len(stack)!=0:
        checked=stack[len(stack)-1]
        stack.pop()
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


def Dijkstra (G,start,end):
    from queue import PriorityQueue
    queue=PriorityQueue()
    n=len(G)
    queue.put((0,start))
    processed=[False for _ in range (n)]
    parents=[[-1,0] for _ in range (n)]
    list_of_priorities=[float('inf') for _ in range (0,n)]
    list_of_priorities[start]=0

    while queue.qsize():
        priority_old,checked=queue.get()
        if processed[checked]==False:
            processed[checked]=True
            for i in range (0,len(G[checked])):
                priority_new=list_of_priorities[G[checked][i][0]]
                distance=G[checked][i][1]
                
                if priority_new>priority_old+distance:
                    priority_new=priority_old+distance
                    new=G[checked][i][0]
                    list_of_priorities[new]=priority_new
                    parents[new][0]=checked
                    parents[new][1]=distance
                    queue.put((priority_new,new))

    return list_of_priorities[end]



def Sections_1(T,a,b):
    #Zlozonosc O(n*log(n))
    
    n=len(T)   
    found=False
    for i in range (n):
        if T[i][0]==a:
            found=True
    if found==False: return False

    found=False
    for i in range (n):
        if T[i][1]==b:
            found=True
    if found==False: return False

    New_T=[[0,0] for _ in range (n)]
    for i in range (n):
        New_T[i][0]=T[i][0]
        New_T[i][1]=T[i][1]
    Conv=[0 for _ in range (2*n)]
    for i in range (n):
        Conv[2*i]=New_T[i][0]
        Conv[2*i+1]=New_T[i][1]
    Perm=[0 for _ in range (2*n)]
    for  i in range (2*n):
        Perm[i]=i
    MergeSort(Conv,Perm)
    curr=-1
    
    for i in range (2*n):
        if Conv[i]<a:
            New_T[Perm[i]//2][0]=None
            New_T[Perm[i]//2][1]=None
        elif Conv[i]>b:
            New_T[Perm[i]//2][0]=None
            New_T[Perm[i]//2][1]=None
        else:
            if New_T[Perm[i]//2][0]!=None:
                if i>0 and Conv[i-1]==Conv[i]:
                    if Perm[i]%2==0:
                        New_T[Perm[i]//2][0]=curr
                    else:
                        New_T[Perm[i]//2][1]=curr
                else:
                    curr+=1
                    if Perm[i]%2==0:
                        New_T[Perm[i]//2][0]=curr
                    else:
                        New_T[Perm[i]//2][1]=curr

    N=curr+1
    G=[[] for _ in range (N)]
    for i in range (n):
        if New_T[i][0]!=None:
            G[New_T[i][0]].append(New_T[i][1])

    return DFS(G,0,N-1)


def Sections_2(T,a,b):
    #Zlozonosc O(n*log(n))
    
    n=len(T)    
    found=False
    for i in range (n):
        if T[i][0][0]==a:
            found=True
    if found==False: return float('inf')

    found=False
    for i in range (n):
        if T[i][0][1]==b:
            found=True
    if found==False: return float('inf')

    New_T=[[0,0] for _ in range (n)]
    for i in range (n):
        New_T[i][0]=T[i][0][0]
        New_T[i][1]=T[i][0][1]
    Conv=[0 for _ in range (2*n)]
    for i in range (n):
        Conv[2*i]=New_T[i][0]
        Conv[2*i+1]=New_T[i][1]
    Perm=[0 for _ in range (2*n)]
    for  i in range (2*n):
        Perm[i]=i
    MergeSort(Conv,Perm)
    curr=-1
    
    for i in range (2*n):
        if Conv[i]<a:
            New_T[Perm[i]//2][0]=None
            New_T[Perm[i]//2][1]=None
        elif Conv[i]>b:
            New_T[Perm[i]//2][0]=None
            New_T[Perm[i]//2][1]=None
        else:
            if New_T[Perm[i]//2][0]!=None:
                if i>0 and Conv[i-1]==Conv[i]:
                    if Perm[i]%2==0:
                        New_T[Perm[i]//2][0]=curr
                    else:
                        New_T[Perm[i]//2][1]=curr
                else:
                    curr+=1
                    if Perm[i]%2==0:
                        New_T[Perm[i]//2][0]=curr
                    else:
                        New_T[Perm[i]//2][1]=curr

    N=curr+1
    G=[[] for _ in range (N)]
    for i in range (n):
        if New_T[i][0]!=None:
            G[New_T[i][0]].append([New_T[i][1],T[i][1]])

    return Dijkstra(G,0,N-1)


def Sections_3(T,k):
    # Zlozonosc O(n^2)
    
    n=len(T)
    Conv_0=[0 for _ in range (n)]
    Conv_1=[0 for _ in range (n)]
    for i in range (n):
        Conv_0[i]=T[i][0]
        Conv_1[i]=T[i][1]
    Rev_Perm_0=[0 for _ in range (n)]
    Rev_Perm_1=[0 for _ in range (n)]
    for i in range (n):
        Rev_Perm_0[i]=i
        Rev_Perm_1[i]=i
    MergeSort(Conv_0,Rev_Perm_0)
    MergeSort(Conv_1,Rev_Perm_1)

    Perm=[[0,0] for _ in range (n)]
    Real_val=[]
    i=0
    j=0
    B=0
    while i<n and j<n:
        if B>0 and Real_val[B-1]==Conv_0[i]:
            Perm[Rev_Perm_0[i]][0]=B-1
            i+=1
        elif B>0 and Real_val[B-1]==Conv_1[j]:
            Perm[Rev_Perm_1[j]][1]=B-1
            j+=1
        else:
            if Conv_0[i]<Conv_1[j]:
                Real_val.append(Conv_0[i])
                Perm[Rev_Perm_0[i]][0]=B
                i+=1
                B+=1
            elif Conv_0[i]==Conv_1[j]:
                Real_val.append(Conv_0[i])
                Perm[Rev_Perm_0[i]][0]=B
                Perm[Rev_Perm_1[j]][1]=B
                i+=1
                j+=1
                B+=1
            elif Conv_0[i]>Conv_1[j]:
                Real_val.append(Conv_1[j])
                Perm[Rev_Perm_1[j]][1]=B
                j+=1
                B+=1
    while i<n:
        if Real_val[B-1]!=Conv_0[i]:
            Real_val.append(Conv_0[i])
            Perm[Rev_Perm_0[i]][0]=B
            i+=1
            B+=1
        else:
            Perm[Rev_Perm_0[i]][0]=B-1
            i+=1
    while j<n:
        if Real_val[B-1]!=Conv_1[j]:
            Real_val.append(Conv_1[j])
            Perm[Rev_Perm_1[j]][1]=B
            j+=1
            B+=1
        else:
            Perm[Rev_Perm_1[j]][1]=B-1
            j+=1

    F=[[float('inf') for _ in range (B)] for _ in range (B)]
    for i in range (n):
        F[Perm[i][0]][Perm[i][1]]=1

    for i in range (1,B):
        for j in range (B-i):
            for p in range (1,i):
                F[j][i+j]=min(F[j][i+j],F[p+j][i+j]+F[j][p+j])

    max_result=-float('inf')
    for i in range (B):
        for j in range (i+1,B):
            if F[i][j]<=k:
                max_result=max(max_result,Real_val[j]-Real_val[i])

    return max_result



task=int(input("Podaj numer zadania: "))
n=int(input("Podaj rozmiar tablicy: "))
T=[]
for i in range (n):
    begin=float(input("Podaj poczatek odcinka dla "+str(i)+" odcinka: "))
    end=float(input("Podaj koniec odcinka dla "+str(i)+" odcinka: "))
    if task==2:
        val=float(input("Podaj koszt "+str(i)+" odcinka: "))
        T.append([(begin,end),val])
    else:
        T.append((begin,end))

if task==3:
    k=int(input("Podaj z ilu conajwyzej odcinkow moze skladac sie przedzial: "))
    print(Sections_3(T,k))
else:
    a=float(input("Podaj poczatek przedzialu: "))
    b=float(input("Podaj koniec przedzialu: "))
    if task==1:
        print(Sections_1(T,a,b))
    if task==2:
        print(Sections_2(T,a,b))
