def knupsuck (W,P,B):
    n=len(W)
    F=[[0 for b in range (B+1)] for i in range (n)]
    for b in range (W[0],B+1):
        F[0][b]=P[0]
    for b in range (B+1):
        for i in range (1,n):
            F[i][b]=F[i-1][b]
            if b-W[i]>=0:
                F[i][b]=max(F[i][b],F[i-1][b-W[i]]+P[i])
    return F[n-1][B]



n=int(input("Podaj liczbe przedmiotow: "))
W=[0 for _ in range (n)]
P=[0 for _ in range (n)]
for i in range (0,n):
    W[i]=int(input("Podaj wage "+str(i)+" przedmiotu: "))
    P[i]=int(input("Podaj cene "+str(i)+" przedmiotu: "))
B=int(input("Podaj maksymalna wage plecaka: "))
print (knupsuck(W,P,B))
