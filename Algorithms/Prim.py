from queue import PriorityQueue

def Prim (G):
    q=PriorityQueue()
    in_tree=[False for _ in range (n)]
    q.put([0,0])
    sum_of_edges=0

    while q.qsize():
        to_add,checked=q.get()
        if in_tree[checked]==False:
            in_tree[checked]=True
            sum_of_edges+=to_add
            for i in range (0, len(G[checked])):
                new=G[checked][i][0]
                if in_tree[new]==False:
                    distance=G[checked][i][1]
                    q.put([distance,new])

    return sum_of_edges




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

result=Prim(G)
print (result)
