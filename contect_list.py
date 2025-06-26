contect_list=[]
contect_list.append(["aman","6203267377","aman@gmail.com","mango"])
contect_list.append(["sneha","9608062292","sneha@gmail.com","sakchi"])
print("for do say yes and for not do say no")

def add():
    name=input("inter name :")
    pno=input("inter pno :")
    gmail=input("inter gmail :")
    addr=input("inter address :")
    contect_list.append([name,pno,gmail,addr])
    opinian=input("for more add say yes and for not say no :")
    if(opinian=="yes"):
        add()
    else:
        return
    
def print_all_contect():
    i=1
    while(i<=len(contect_list)):
        print(contect_list[i-1])
        i+=1

def remove():
    remove1=int(input("inter index no of list which are you want to remove :"))
    contect_list.remove(contect_list[remove1])
    opinian=input("for more remove say yes and no say no :")
    if(opinian=="yes"):
        remove()
    else:
        return

def search():
    search1=input("inter name or phone number which are you want to remove :")
    j=0
    while(j<=len(contect_list)-1):
        k=0
        while(k<=3):
            if(search1==contect_list[j][k]):
                print(contect_list[j])
                break
            k+=1
        j+=1
    opinian=input("for more search say yes and no say no :")
    if(opinian=="yes"):
        search()
    else:
        return
    
def update():
    update1=int(input("inter first index number which you want to update :"))
    update2=int(input("inter second index number which you want to update :"))
    contect_list[update1][update2]=input("inter updation :")
    opinian=input("for more update say yes and no say no :")
    if(opinian=="yes"):
        update()
    else:
        return

x=input("\nare you add contect :")
if(x=="yes"):
    add()

y=input("\nare you remove some specific contect :")
if(y=="yes"):
    remove()

p=input("\nare you update some specific contect :")
if(p=="yes"):
    update()

z=input("\nare you search some specific contect :")
if(z=="yes"):
    search()

q=input("\nare you print contect list :")
if(q=="yes"):
    print_all_contect()    



    