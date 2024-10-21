
def Tasks(T):
    n=len(T)
    last=T[n-1][0]
    Task=[None for _ in range (last+1)]
    Profit=[0 for _ in range (last+1)]
    
    for i in range (n):
        if T[i][1]>Profit[T[i][0]]:
            Profit[T[i][0]]=T[i][1]
            Task[T[i][0]]=i

    Result=[]
    for i in range (1,last+1):
        if Task[i]!=None:
            Result.append(Task[i])
            
    return Result


n=int(input("Podaj rozmiar tablicy: "))
T=[]
for i in range (n):
    date=int(input("Podaj termin dla "+str(i)+" zadania: "))
    reward=int(input("Podaj nagrode za "+str(i)+" zadanie: "))
    T.append((date,reward))
print (Tasks(T))
    
    
    
