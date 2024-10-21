from queue import PriorityQueue

def Dijkstra (G,start,end,full_list):
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
                

    if full_list==0:
        if parents[end][0]==-1:
            return None
        
        result=0
        travel=end
        while start!=travel:
            result+=parents[travel][1]
            travel=parents[travel][0]
        return result

    else:
        return list_of_priorities








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

start=int(input("Podaj nazwe wierzcholka startowego: "))
full_list=int(input("Wcisnij 0 jesli chcesz znalezc droge tylko do 1 wierzcholka, w przeciwnym wypadku wcisnij 1: "))
if full_list==0:
    end=int(input("Podaj nazwe wierzcholka koncowego: "))
else:
    end=0

result=Dijkstra(G,start,end,full_list)
print (result)
        
