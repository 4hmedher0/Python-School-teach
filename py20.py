cakes=float (input("enter number of Cakes "))
result =(cakes/48)
sugar=format(1.5*result,'.2f')
butter=format(1*result,'.1f')
floor=format(2.75*result,'.2f')
print("sugar :",sugar,"kg")
print("butter :",butter,"kg")
print("floor :",floor,"kg")
for i in range(2,8):
    print(i)
