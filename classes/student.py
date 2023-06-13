class Student:
    school="AkiraChix"
    def __init__(self,name,age,country):
        self.name=name
        self.age=age
        self.country=country

    def great_student(self):
        return f"Hello {self.name} from {self.country} welcome to {self.school}"        

