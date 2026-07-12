import random

a = [1,2,3,4,5,6,7,8,9,10] 

computer = random.randint(1,10) 



def f() : 
    i = 0 
    while True :
        user = int(input(f"Enter a number from {a} : ")) 
        i += 1
        if user > computer and user in a :
            print (" choose a lower number !!! ") 
        elif computer > user and user in a :
            print (" choose a higher number !!! ") 
        elif user not in  a :
            print (f"choose a number from : {a}")
        elif user == computer :
            print (f" YAY YOU WON \nYou won in {i} attempts ")
            break
f()