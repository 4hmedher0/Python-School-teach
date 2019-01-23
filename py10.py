from datetime import *
day=datetime.today()#allcoate datetime in day vari
print(day.strftime("%a"))#day
print(day.strftime("%b"))#month
print(day.strftime("%c"))#full data str and number
print(day.strftime("%y"))#year
print(day.month)
print(day.hour)
print(day.day)
print(day.today())
year=day.year
while True:
  dob=int(input("enter date of birth "))
  #int(year)=day.year
  age=int(year)-int(dob)
  print("your age is :",age)
      
