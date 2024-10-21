def Longest_Ascending_Substring (A):
    n=len(A)
    F=[1]*n
    parents=[-1]*n
    read_substring=[]
    for i in range (1,n):
        F[i]=F[i-1]
        for j in range (i):
            if A[j]<A[i] and F[j]+1>F[i]:
                parents[i]=j
                F[i]=F[j]+1

    for i in range (n-1,-1,-1):
        current=i
        if parents[i]!=-1:
            break

    while parents[current]!=-1:
        read_substring.append(A[current])
        current=parents[current]
    read_substring.append(A[current])
    read_substring.reverse()
    
    return max(F),read_substring



n=int(input("Podaj dlugosc tablicy: "))
A=[0 for _ in range (n)]
for i in range (0,n):
    A[i]=int(input("Podaj "+str(i)+" element tablicy: "))

length,substring=Longest_Ascending_Substring(A)
print (length)
print (substring)
