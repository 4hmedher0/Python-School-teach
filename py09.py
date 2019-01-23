file=open("password.txt",'w')#write
file.write("user\n pass\n addrese\n end")
file.close()
file2=open("password.txt",'r')#read
data=file2.read()
import sys
for i in data:
  #print(i)
  sys.stdout.write(i)
  if i=='r':
      pass

      #print('ww')
      
file2.close()
file3=open("names","w")
data=file3.write=("\nmeddo\n ali\n gaber\nzewill")
file3=open("names","r")
for i in data:
   sys.stdout.write(i)
   #print(i)
print(file3.read())   
file3.close()
#getfilename=input("enter file name: ")
file0=open("ddd.txt","r")
print(file0)
file0.close()

