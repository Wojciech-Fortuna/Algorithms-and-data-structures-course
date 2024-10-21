
def Petrol_1(D,F,L):
    position=0
    petrol=min(F[0],L)
    result=0
    n=len(D)
    if n==1: return 0
    
    while D[n-1]-D[position]>petrol:
        result+=1
        i=position
        max_petrol=0
        next_station=None
        while D[i+1]-D[position]<=petrol:
            i+=1
            distance=D[i]-D[position]
            if F[i]+petrol>=max_petrol:
                max_petrol=min(F[i]+petrol,L-petrol+distance)
                next_station=i
        position=next_station
              
        if next_station==None:
            return float('inf')
        distance=D[next_station]-D[position]
        petrol=max_petrol-distance

    result+=1
    return result


def Petrol_2(D,F,P,L):
    n=len(D)
    A=[[float('inf') for _ in range (L+1)] for _ in range (n)]
    A[0][0]=0
    if F[0]==0: return 0
    for i in range (1,min(F[0]+1,L+1)):
        A[0][i]=P[0]*i/F[0]

    for i in range (1,n):
        distance=D[i]-D[i-1]
        for j in range (L+1):
            if j+distance<=L:
                A[i][j]=A[i-1][j+distance]
        for j in range (L,-1,-1):
            if F[i]>0:
                for k in range (1,F[i]+1):
                    if j-k>=0:
                        price=P[i]*k/F[i]
                        A[i][j]=min(A[i][j],A[i][j-k]+price)

    return A[n-1][0]


def Petrol_3(D,F,P,L):
    n=len(D)
    A=[[float('inf') for _ in range (L+1)] for _ in range (n)]
    if F[0]==0: return 0
    if F[0]>L: return float('inf')
    A[0][0]=0
    A[0][F[0]]=P[0]

    for i in range (1,n):
        distance=D[i]-D[i-1]
        for j in range (L+1):
            if j+distance<=L:
                A[i][j]=A[i-1][j+distance]
        for j in range (L,-1,-1):
            if j-F[i]>=0:
                A[i][j]=min(A[i][j],A[i][j-F[i]]+P[i])
  
    min_val=float('inf')
    for i in range (L+1):
        min_val=min(min_val,A[n-1][i])
    return min_val



task=int(input("Podaj numer zadania: "))
n=int(input("Podaj rozmiar tablicy: "))
D=[0 for _ in range (n)]
F=[0 for _ in range (n)]
if task!=1:
    P=[0 for _ in range (n)]
for i in range (n):
    if i!=0:
        D[i]=int(input("Podaj odleglosc poczatkowej stacji od "+str(i)+" stacji: "))
    F[i]=int(input("Podaj ilosc paliwa na "+str(i)+" stacji: "))
    if task!=1:
        P[i]=int(input("Podaj cene za cale paliwo na "+str(i)+" stacji: "))
L=int(input("Podaj pojemnosc baku: "))
if task==1:
    print (Petrol_1(D,F,L))
if task==2:
    print (Petrol_2(D,F,P,L))
if task==3:
    print (Petrol_3(D,F,P,L))
    

        
