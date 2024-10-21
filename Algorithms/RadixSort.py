def RadixSort (A):
    n=len(A)
    max_length=len(A[0])
    for i in range (1,n):
        if max_length<len(A[i]):
            max_length=len(A[i])
            
    min_ord=None
    max_ord=None
    for word in range (0,n):
        for letter in range (0,len(A[word])):
            if min_ord==None or min_ord>ord(A[word][letter]):
                min_ord=ord(A[word][letter])
            if max_ord==None or max_ord<ord(A[word][letter]):
                max_ord=ord(A[word][letter])

    C_table_size=max_ord-min_ord+2
    for letter in range (max_length-1,-1,-1):
        C=[0]*C_table_size
        B=[0]*n
        for i in range (n):
            if letter>len(A[i])-1:
                C[0]+=1
            else:
                C[ord(A[i][letter])-min_ord+1]+=1
        for i in range (1,C_table_size):
            C[i]=C[i]+C[i-1]
        for i in range (n-1,-1,-1):
            if letter>len(A[i])-1:
                B[C[0]-1]=A[i]
                C[0]-=1
            else:
                B[C[ord(A[i][letter])-min_ord+1]-1]=A[i]
                C[ord(A[i][letter])-min_ord+1]-=1
        for i in range (n):
            A[i]=B[i]



n=int(input("Podaj wielkosc tablicy: "))
A=[0 for _ in range (n)]
for i in range (0,n):
    A[i]=str(input("Podaj "+str(i)+" napis: "))

RadixSort(A)
print (A)

