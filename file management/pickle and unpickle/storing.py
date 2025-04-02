import Student, pickle

studs = [Student.student(10, 'Yash Goel','CSE'), Student.student(11,'Abdul','Mechanical'),Student.student(14,'Aalok','CSE')]

with open('students.data','wb') as f:
    for s in studs:
        pickle.dump(s,f)