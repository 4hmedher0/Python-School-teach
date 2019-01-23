class student:
    def __init__(self,name,course):#constructor
      self.name=name
      self.course=course
      self.money=900
      print("welcome to my class")

    def mark (self,char1):
        self.char1=char1
        if char1>=50 and char1<60:print("D")
        elif char1>=60and char1<70:print("C")
        elif char1>=70and char1<80:print("B")
        elif char1>=80and char1<90:print("A")
        elif char1>=90 and char1<=100:print("A+")
        else:print("unknown")
                                          
        
