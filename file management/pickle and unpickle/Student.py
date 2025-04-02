class student:
    def __init__(self,rollnum,name,course):
        self.rollnum = rollnum
        self.name = name
        self.course = course
    def display(self):
        print(f"My name is {self.name}, roll number: {self.rollnum} and I have completed {self.course}")