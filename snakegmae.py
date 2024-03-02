import random
def check(computer,user):
    if computer == user :
        return 0
    if computer == 2 and  user == 1:
        return  -1
    if computer == 1 and  user == 0:
        return  -1
    if computer == 2 and  user == 0:
        return  -1
    return 1
computer=(random.randint(0,2))
def a(check):
    if computer==0 :
        print("rock")
    if computer==1 :
        print("paper") 
    if computer== 2:
        print("sesor")
user = int(input("0 for rock , 1 for paper , 2 for sesor:\n"))
print("you:- ", user)
print("computer:- ", computer)
score = check( computer , user )
if score == 0 :
    print("its a drow ")
elif score == -1 :
    print ("you lose")
else :
    print( "you win ")