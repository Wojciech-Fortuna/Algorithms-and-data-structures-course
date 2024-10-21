class Employee:
    def __init__ (self,name,fun,subordinates):
        self.name=name
        self.fun=fun
        self.emp=subordinates
        self.f=-1
        self.g=-1

def f(v):
    if v.f>=0:
        return v.f
    x=v.fun
    for ui in v.emp:
        x+=g(ui)
    y=g(v)
    v.f=max(x,y)
    return v.f

def g(v):
    if v.g>=0:
        return v.g
    x=0
    for vi in v.emp:
        x+=f(vi)
    v.g=x
    return v.g


def create_company(boss,list_of_names):
    boss.fun=int(input("Podaj poziom imprezowosci dla "+boss.name+": "))
    n=int(input("Podaj liczbe podwladnych dla "+boss.name+": "))
    subordinates=[]
    for i in range (0,n):
        while True:
            new_emp_name=input("Podaj nazwe "+str(i)+" podwladnego dla "+boss.name+": ")
            if new_emp_name in list_of_names:
                print ("Ten pracownik jest juz przydzielony")
            else:
                list_of_names.append(new_emp_name)
                break
        new_emp=Employee(new_emp_name,0,[])
        create_company(new_emp,list_of_names)
        subordinates.append(new_emp)
    boss.emp=subordinates







boss_name=input("Podaj nazwe najwyzszego szefa: ")
list_of_names=[boss_name]
boss=Employee(boss_name,0,[])
create_company(boss,list_of_names)
print (f(boss))

