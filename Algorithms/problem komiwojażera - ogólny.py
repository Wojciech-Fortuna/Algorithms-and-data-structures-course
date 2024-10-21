from math import sqrt

def GetElements(code):
    curr_set=[]
    elem=1
    while code!=0:
        if code%2==1:
            curr_set.append(elem)
        code=code//2
        elem+=1
    return curr_set


def distance(elem1,elem2,T):
    a=T[elem1][0]-T[elem2][0]
    b=T[elem1][1]-T[elem2][1]
    return sqrt((a**2)+(b**2))




def Komiwojazer(T):
    n=len(T)
    if n<2: return 0
    F=[[float('inf') for _ in range (n)] for _ in range (2**(n-1))]
    for i in range (n):
        F[0][i]=distance(0,i,T)
    for set_code in range (1,2**(n-1)):
        curr_set=GetElements(set_code)
        size_of_set=len(curr_set)
        for add_elem in range (1,n):
            min_val=float('inf')
            for i in range (0,size_of_set):
                checked_elem=curr_set[i]
                new_set_code=set_code-(2**(checked_elem-1))
                min_val=min(min_val,F[new_set_code][checked_elem]+distance(add_elem,checked_elem,T))
            F[set_code][add_elem]=min_val

    result=float('inf')
    for i in range (1,n):
        result=min(result,F[(2**(n-1))-1][i]+distance(i,0,T))
    return result



n=int(input("Podaj liczbe miast: "))
T=[]
for i in range (n):
    d=int(input("Podaj dlugosc geograficzna dla miasta "+str(i)+": "))
    s=int(input("Podaj szerokosc geograficzna dla miasta "+str(i)+": "))
    T.append((d,s))
print (Komiwojazer(T))

                
            
                
