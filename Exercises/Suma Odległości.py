
def Sum(A):
    return A[len(A)//2]


n=int(input("Podaj rozmiar tablicy: "))
A=[0 for _ in range (n)]
for i in range (n):
    A[i]=float(input("Podaj "+str(i)+" element: "))
print (Sum(A))
