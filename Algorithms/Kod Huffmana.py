
def Huffman(T):
    n=len(T)
    m=n
    if n==1: return [0]
    Prob=T.copy()
    children=[() for _ in range (n)]
    Code=[None for _ in range (2*n-1)]

    while True:
        min1=float('inf')
        min1_idx=0
        for i in range (m):
            if Prob[i]<min1:
                min1_idx=i
                min1=Prob[i]
        min2=float('inf')
        min2_idx=0
        for i in range (m):
            if i!=min1_idx and Prob[i]<min2:
                min2_idx=i
                min2=Prob[i]
        if min2==float('inf'):
            center=min1_idx
            break

        Prob[min1_idx]=float('inf')
        Prob[min2_idx]=float('inf')
        Prob.append(min1+min2)
        children.append((min2_idx,min1_idx))
        m+=1

    Create_code(center,Code,children)
    return Code[:n]


def Create_code(idx,Code,children):
    if len(children[idx])!=0:
        curr_code=Code[idx]
        if curr_code!=None:
            Code[children[idx][0]]=curr_code+str(0)
            Code[children[idx][1]]=curr_code+str(1)
            Create_code(children[idx][0],Code,children)
            Create_code(children[idx][1],Code,children)
        else:
            Code[children[idx][0]]=str(0)
            Code[children[idx][1]]=str(1)
            Create_code(children[idx][0],Code,children)
            Create_code(children[idx][1],Code,children)





n=int(input("Podaj liczbe znakow: "))
Names=[]
T=[]
for i in range (n):
    Names.append(input("Podaj "+str(i)+" znak: "))
    T.append(float(input("Podaj prawdopodobienstwo wystapienia dla "+str(i)+" znaku: ")))
Result_array=Huffman(T)
for i in range (n):
    print (Names[i]+" -> "+str(Result_array[i]))
    
