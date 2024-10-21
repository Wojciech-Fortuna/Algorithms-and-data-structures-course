def MergeSort (T):
    if len(T)>1:
        mid=len(T)//2
        L=T[:mid]
        R=T[mid:]
        MergeSort(L)
        MergeSort(R)
        i=j=k=0

        while i<len(L) and j<len(R):
            if L[i][0]<=R[j][0]:
                T[k]=L[i].copy()
                i+=1
            else:
                T[k]=R[j].copy()
                j+=1
            k+=1

        while i<len(L):
            T[k]=L[i].copy()
            i+=1
            k+=1

        while j<len(R):
            T[k]=R[j].copy()
            j+=1
            k+=1


def Kruskal(G):
    n=len(G)
    edges=[]
    result_edges=[]
    for i in range (0,n):
        for j in range (0,len(G[i])):
            edges.append([G[i][j][1], i, G[i][j][0]])
    MergeSort(edges)

    set_size=[1 for _ in range (0,n)]
    set=[0 for _ in range (n)]
    for i in range (0,n):
        set[i]=i

    number_of_edge=0 
    number_of_sets=n
    while number_of_sets>1 and number_of_edge<len(edges):
        first=edges[number_of_edge][1]
        second=edges[number_of_edge][2]

        begin=first        
        while set[first]!=first:
            first=set[first]
        root_first=first
        while set[begin]!=begin:
            next=set[begin]
            set[begin]=root_first
            begin=next

        begin=second
        while set[second]!=second:
            second=set[second]
        root_second=second
        while set[begin]!=begin:
            next=set[begin]
            set[begin]=root_second
            begin=next

        if root_first!=root_second:
            if set_size[root_first]>set_size[root_second]:
                set[root_second]=root_first
                set_size[root_first]+=set_size[root_second]
            else:
                set[root_first]=root_second
                set_size[root_second]+=set_size[root_first]
            number_of_sets-=1
            result_edges.append([edges[number_of_edge][1], edges[number_of_edge][2]])
        number_of_edge+=1

    return result_edges




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

result=Kruskal(G)
print (result)
        
