class student:
    def __init__(self,name):
        self.name=name
        self.mark=[]
        print("welcome {} to your school ".format(name))
    def addm(self,mark):
        self.mark.append(mark)
    def ave (self):
        return sum(self.mark)/len(self.mark)
