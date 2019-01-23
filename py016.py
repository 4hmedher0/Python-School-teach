stop=True
while stop :
 def tea ():
    print("boil water")
    print("put sugar,")
    print("use spoon")
    print("drink tea")
 def coffe():
    mix()
    print("drink Coffe")

 def mix():
    print("boil water")
    print("put sugar,")
    print("use spoon")
 name=input("enter your name ")
 if name=="medo":coffe()
 elif name=="ahmed":tea()
 else:
     print("Drink water")
     stop=False

          

