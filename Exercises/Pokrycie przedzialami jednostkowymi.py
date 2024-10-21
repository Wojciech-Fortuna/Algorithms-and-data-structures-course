
def Coverage (T):
    n=len(T)
    result=1
    begin=T[0]
    for i in range (n):
        if T[i]>begin+1:
            begin=T[i]
            result+=1
    return result


n=int(input("Podaj rozmiar tablicy: "))
T=[0 for _ in range (n)]
for i in range (n):
    T[i]=float(input("Podaj "+str(i)+" punkt: "))
print (Coverage(T))
