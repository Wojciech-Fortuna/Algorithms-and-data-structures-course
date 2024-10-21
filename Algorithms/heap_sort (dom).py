def left (i):
    return (2*i+1)

def right (i):
    return (2*i+2)

def parent (i):
    return (i-1)//2



def heapify (S, n, i):
    l=left(i)
    r=right(i)
    max_ind=i
    if l<n and S[l]>S[max_ind]:
        max_ind=l
    if r<n and S[r]>S[max_ind]:
        max_ind=r

    if max_ind!=i:
        S[i],S[max_ind]=S[max_ind],S[i]
        heapify (S,n, max_ind)

def build_heap (S):
    n=len(S)
    for i in range (n//2-1, -1, -1):
        heapify (S,n,i)

def heap_sort (S):
    n=len(S)
    build_heap(S)
    for i in range (n-1,0,-1):
        S[0],S[i]=S[i],S[0]
        heapify (S,i,0)

n=int(input("Podaj wielkosc tablicy: "))
S=[0 for _ in range (n)]
for i in range (0,n):
    S[i]=int(input("Podaj "+str(i)+" liczbe: "))

heap_sort(S)
print (S)
