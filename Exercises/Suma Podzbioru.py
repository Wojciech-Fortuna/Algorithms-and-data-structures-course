
def sub_sum(T,B):
    n=len(T)
    F=[[False for _ in range (B+1)] for _ in range (n)]
    for i in range (n):
        if T[i]<=B:
            F[i][T[i]]=True

    for i in range (1,n):
        for j in range (B+1):
            if j-T[i]>=0:
                F[i][j]=F[i-1][j] or F[i-1][j-T[i]]
            else:
                F[i][j]=F[i-1][j]

    return F[n-1][B]



n=int(input("Podaj liczbe elementow: "))
T=[0 for _ in range (n)]
for i in range (n):
    T[i]=int(input("Podaj "+str(i)+" element: "))
B=int(input("Podaj sume do jakiej maja sie sumowac elementy: "))
print (sub_sum(T,B))
