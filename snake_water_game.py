import random           #random module genrated random number according to range 
def game(computer,player):      #function definition
    if computer==player:
        return None
    elif computer=='s':
        if player=='w':
            return False
        elif player=='g':
            return True
    elif computer=='w':
        if player=='s':

            return True
        elif player=='g':
            return False
    elif computer=='g':
        if player=='w':
            return True
        elif player=='s':
            return False
        

print("computer choose : snake(s),water(w) and gun(g)")         
rand_num=random.randint(1,3)                            #genrated by computer 1 to 3 
if rand_num==1:
    computer='s'
elif rand_num==2:
    computer='w'
elif rand_num==3:
    computer='g'

player=input("player choose : : snake(s),water(w) and gun(g)\n")        #user input

a=game(computer,player)         #call function game with parameter
if a==None:
    print("match will be tie!")
elif a==True:
    print("YOU WIN !")
else:
    print("YOU LOSE !")

print(f"computer choose:{computer}")
print(f"player choose:{player} ")
