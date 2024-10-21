
def Longest_Common_Subsequence(A,B):
    F=[[0 for _ in range (len(B))] for _ in range (len(A))]

    for i in range (len(A)):
        for j in range (len(B)):
            if i==0 or j==0:
                if i>0:
                    F[i][j]=F[i-1][j]
                if j>0:
                    F[i][j]=F[i][j-1]
                if A[i]==B[j]:
                    F[i][j]=max(F[i][j],1)
            else:
                if A[i]==B[j]:
                    F[i][j]=max(F[i-1][j],F[i][j-1],F[i-1][j-1]+1)
                else:
                    F[i][j]=max(F[i-1][j],F[i][j-1])

    return F[len(A)-1][len(B)-1]



n=int(input("Podaj liczbe elementow w tablicy A: "))
A=[0 for _ in range (n)]
for i in range (n):
    A[i]=int(input("Podaj "+str(i)+" element w tablicy A: "))
n=int(input("Podaj liczbe elementow w tablicy B: "))
B=[0 for _ in range (n)]
for i in range (n):
    B[i]=int(input("Podaj "+str(i)+" element w tablicy B: "))
print (Longest_Common_Subsequence(A,B))
