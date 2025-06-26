a=float(input("inter the first number :"))
b=float(input("inter the second number :"))
x=input("inter the operator :")
if(x=="+"):
    add1=float(a+b)
    add2=int(a+b)
    if(add1==add2):
        print("result is :",add2)
    else:
        print("result is :",add1)

elif(x=="-"):
    sub1=float(a-b)
    sub2=int(a-b)
    if(sub1==sub2):
        print("result is :",sub2)
    else:
        print("result is :",sub1)     

elif(x=="*"):
    mul1=float(a*b)
    mul2=int(a*b)
    if(mul1==mul2):
        print("result is :",mul2)
    else:
        print("result is :",mul1)

elif(x=="/"):
    div1=float(a/b)
    div2=int(a/b)
    if(div1==div2):
        print("result is :",div2)
    else:
        print("result is :",div1)

else:
    print("operator is not valid for calculator..")
