#FIRST gAME gHOST
from random import randint
from datetime import *
day=datetime.today()
print("\t{X}Welcom To Cave Of Ghosts {X}\t")
score=0
i=True
while i:
  userchoose=input("\tEnter Number Of Room:\t")  
  ghostroom=randint(1,3)  
  if int(userchoose)==ghostroom:
    print("\t\n\aGhooOooooost Catch you\n")
    i=False
  else:
    print("\tyou are so Lucky this time,Try again")
    score+=1

print("\t{X}Game Over {X}\n")
print("\tyou have Scored :",score)
print("time now: ",day)
