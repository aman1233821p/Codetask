import string
import random
opinian=input("for only choose password length say yes otherwise no :")
password=""

if(opinian=="yes"):
    password_length=int(input("inter the password length :"))
    alp=random.randint(0,password_length)
    digit=random.randint(0,password_length-alp)
    symbol=password_length-(alp+digit)

elif(opinian=="no"):
    alp=int(input("choose no of alphabet :"))
    digit=int(input("choose no of digits :"))
    symbol=int(input("choose no of symbols :"))

i=1
while(i<=alp):
    rand1=random.randint(0,51)
    password=password+string.ascii_letters[rand1]
    i+=1

j=1
while(j<=digit):
    rand2=random.randint(0,9)
    password=password+string.digits[rand2]
    j+=1

k=1
while(k<=symbol):
    rand3=random.randint(0,31)
    password=password+string.punctuation[rand3]
    k+=1

password=list(password)
random.shuffle(password)
password="".join(password)
print("your password is :",password)





