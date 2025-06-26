import random
class marks:
    def marks1(self):
        self.your_marks+=1
    def marks2(self):
        self.computer_marks+=1
object=marks()
object.your_marks=0
object.computer_marks=0

y=["rock","paper","scissor"]

i=1
while(i>0):
    x=input("inter your choice :")
    z=random.randint(0,2)
    p=y[z]
    if(x=="rock"):
        print("computer choice :",p)
        if(p=="rock"):
            print("game is tie")
            print("\n")
        elif(p=="paper"):
            print("computer win")
            print("\n")
            object.marks2()
            say=input("for restart say yes for quit say no\ndo you want to play more :")
            if(say=="yes"):
                print("\n")
                pass
            else:
                print("\n")
                print("your marks=",object.your_marks)
                print("computer marks=",object.computer_marks)
                input("give your feedback :")
                print("thank you for your response.")
                break
        else:
            print("you win")   
            print("\n")
            object.marks1()
            say=input("for restart say yes and for quit say no\ndo you want to play more :")
            if(say=="yes"):
                print("\n")
                pass
            else:
                print("\n")
                print("your marks=",object.your_marks)
                print("computer marks=",object.computer_marks)
                input("give your feedback :")
                print("thank you for your response.")
                break
    elif(x=="paper"):
        print("computer choice :",p)       
        if(p=="rock"):
            print("you win")
            print("\n")
            object.marks1()
            say=input("for restart say yes and for quit say no\ndo you want to play more :")
            if(say=="yes"):
                print("\n")
                pass
            else:
                print("\n")
                print("your marks=",object.your_marks) 
                print("computer marks=",object.computer_marks) 
                input("give your feedback :")
                print("thank you for your response.")
                break
        elif(p=="paper"):
            print("game is tie")
            print("\n")
        else:
            print("computer win")
            print("\n")
            object.marks2()
            say=input("for restart say yes and for quit say no\ndo you want to play more :")
            if(say=="yes"):
                print("\n")
                pass
            else:
                print("\n")
                print("your marks=",object.your_marks)
                print("computer marks=",object.computer_marks)
                input("give your feedback :")
                print("thank you for your response.")
                break
    elif(x=="scissor"):
        print("computer choice :",p)    
        if(p=="rock"):
            print("computer win")
            print("\n")
            object.marks2()
            say=input("for restart say yes and for quit say no\ndo you want to play more :")
            if(say=="yes"):
                print("\n")
                pass
            else:
                print("\n")
                print("your marks=",object.your_marks) 
                print("computer marks=",object.computer_marks) 
                input("give your feedback :")
                print("thank you for your response.")
                break
        elif(p=="paper"):
            print("you win")
            print("\n")
            object.marks1()
            say=input("for restart say yes and for quit say no\ndo you want to play more :")
            if(say=="yes"):
                print("\n")
                pass
            else:
                print("\n")
                print("your marks=",object.your_marks) 
                print("computer marks=",object.computer_marks) 
                input("give your feedback :")
                print("thank you for your response.")
                break
        else:
            print("game is tie")
            print("\n")
    else:
        print("\n")
        print("your choice is wrong")
        print("please choose 'rock' or 'paper' or 'scissor'")     
    i+=1            



            
    

            