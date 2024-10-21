def Euler_nieskierowany(G):
    stack=[0]
    n=len(G)
    proceeded=[0 for _ in range (n)]
    result=[]

    while len(stack)!=0:
        checked=stack[len(stack)-1]
        if proceeded[checked]==len(G[checked]):
            stack.pop()
            result.append(checked)
        else:
            next_vertex=G[checked][proceeded[checked]]
            if proceeded[next_vertex]==len(G[next_vertex]):
                proceeded[checked]+=1
            elif checked<G[next_vertex][proceeded[next_vertex]]:
                proceeded[checked]+=1
            else:
                proceeded[checked]+=1
                stack.append(next_vertex)

    return result

def Euler_skierowany(G):
    stack=[0]
    n=len(G)
    proceeded=[0 for _ in range (n)]
    result=[]

    while len(stack)!=0:
        checked=stack[len(stack)-1]
        if proceeded[checked]==len(G[checked]):
            stack.pop()
            result.append(checked)
        else:
            next_vertex=G[checked][proceeded[checked]]
            proceeded[checked]+=1
            stack.append(next_vertex)

    result.reverse()
    return result









skierowany=int(input("wcisnij 1 jesli bedzie to graf skierowany, wcisnij 0 jesli bedzie to graf nieskieroawny: "))
n=int(input("Podaj liczbe wierzcholkow w grafie: "))
print ("")
G=[[] for _ in range (n)]
for i in range (n):
    m=int(input("Podaj liczbe sasiadow "+str(i)+" wierzcholka: "))
    for j in range (m):
        nazwa=int(input("Podaj nazwe "+str(j)+" sasiada "+str(i)+" wierzcholka: "))
        G[i].append(nazwa)
    print ("")

if skierowany==0:
    result=Euler_nieskierowany(G)
else:
    result=Euler_skierowany(G)
print (result)
