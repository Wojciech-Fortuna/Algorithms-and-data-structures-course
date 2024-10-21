
def Prom(A,L):
    if A[0]>L: return [],[]
    n=len(A)
    F=[[False for _ in range (L+1)] for _ in range (n)]
    sum_len=[0 for _ in range (n)]
    sum_len[0]=A[0]
    for i in range (1,n):
        sum_len[i]=sum_len[i-1]+A[i]
    F[0][L-A[0]]=True
    F[0][L]=True
    last_car=[0,L-A[0]]
    left=[]
    right=[]

    car_no=0
    space=True
    while space==True and car_no+1<n:
        space=False
        car_no+=1
        for i in range (L+1):
            if i+A[car_no]<=L and F[car_no-1][i+A[car_no]]==True:
                F[car_no][i]=True
            if F[car_no-1][i]==True and sum_len[car_no]+i<=2*L:
                F[car_no][i]=True
            if F[car_no][i]==True:
                space=True
                last_car=[car_no,i]
        if space==False:
            car_no-=1

    for i in range (car_no,0,-1):
        if F[i-1][last_car[1]]==True:
            right.append(i)
            last_car[0]-=1
        else:
            left.append(i)
            last_car[0]-=1
            last_car[1]+=A[i]

    if last_car[1]==L:
        right.append(0)
    else:
        left.append(0)
    left.reverse()
    right.reverse()

    return left,right




n=int(input("Podaj rozmiar tablicy: "))
T=[0 for _ in range (n)]
for i in range (n):
    T[i]=int(input("Podaj romiar "+str(i)+" auta: "))
L=int(input("Podaj wielkosc pojedynczego pasa: "))
Left,Right=Prom(T,L)
print ("Lewy pas: "+str(Left))
print ("Prawy pas: "+str(Right))
