
def Klocki(T):
    F=[0 for _ in range (n)]
    for i in range (n-1,-1,-1):
        min_val=0
        for j in range (i,n):
            if T[i][0]<=T[j][0] and T[i][1]>=T[j][1]:
                min_val=max(min_val,F[j])
        F[i]=min_val+1

    max_num=-float('inf')
    for i in range (0,n):
        max_num=max(max_num,F[i])
    return n-max_num


n=int(input("Podaj rozmiar tablicy: "))
T=[]
for i in range (n):
    start=int(input("Podaj poczatek "+str(i)+" przedzialu: "))
    stop=int(input("Podaj koniec "+str(i)+" przedzialu: "))
    T.append((start,stop))
print (Klocki(T))
