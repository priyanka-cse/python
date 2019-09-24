class University:
    def __init__(self):
        self.sid=" "
        self.age=0
        self.marks=0
    def validate_marks(self):
        if self.marks<0 or self.marks>100:
            return False
        else:
            return True
    def validate_age(self):
        if self.age < 20:
            return False
        else:
            return True
    def check_qualification(self):
        if self.validate_marks() and self.validate_age():
            if self.marks>60:
                return True
        else:
            return False
    def set_data(self,sid,age,marks):
        self.sid=sid
        self.age=age
        self.marks=marks
    def get_data(self):
        print("Name:",self.sid)
        print("Age:",self.age)
        print("Marks:",self.marks)
        if self.check_qualification():
            print("validated")
        else:
            print("Not qualified")
n=int(input("enter how many students:"))
for i in range(n):
    obj=University()
    StudId=input("enter su\tudent id")
    Sage=int(input("enter the age"))
    Marks=int(input("Enter the marks"))
    obj.set_data(StudId,Sage,Marks)
    obj.get_data()
obj.get_data()
        

