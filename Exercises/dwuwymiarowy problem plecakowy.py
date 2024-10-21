
def knupsuck (w,h,v,W,H):
    n=len(v)
    F=[[[0 for _ in range (H+1)] for _ in range (W+1)] for _ in range (n)]
    for i in range (w[0],W+1):
        for j in range (h[0],H+1):
            F[0][i][j]=v[0]
    for i in range (1,n):
        for j in range (W+1):
            for k in range (H+1):
                F[i][j][k]=F[i-1][j][k]
                if j-w[i]>=0 and k-h[i]>=0:
                    F[i][j][k]=max(F[i][j][k],F[i-1][j-w[i]][k-h[i]]+v[i])
    return F[n-1][W][H]



n=int(input("Podaj liczbe przedmiotow: "))
v=[0 for _ in range (n)]
w=[0 for _ in range (n)]
h=[0 for _ in range (n)]
for i in range (0,n):
    w[i]=int(input("Podaj wage "+str(i)+" przedmiotu: "))
    h[i]=int(input("Podaj wysokosc "+str(i)+" przedmiotu: "))
    v[i]=int(input("Podaj cene "+str(i)+" przedmiotu: "))
W=int(input("Podaj maksymalna wage plecaka: "))
H=int(input("Podaj maksymalna wysokosc plecaka: "))
print (knupsuck(w,h,v,W,H))
