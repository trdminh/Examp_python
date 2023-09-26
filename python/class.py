class Student:
    def __init__(self,name,grade,school,cls):
        self.name = name
        self.grade = grade
        self.school = school
        self.cls = cls
    def getInfor(self):
        print(f"The information of {self.name}:\n")
        print(f"{self.name},class {self.cls},grade {self.grade},{self.school} school")
if __name__ == '__main__':
    
    student_1 = Student('Minh',12,'Le Hong Phong High','Math')

    student_1.getInfor()
        