class Student:
    def  __init__(self,name,major,code_portfolio_score,group_project_score,exam_score):
        self.name = name
        self.major = major
        self.code_portfolio_score = code_portfolio_score
        self.group_project_score = group_project_score
        self.exam_score =exam_score
    #define a function that can collect the student information
    def info_student(self):
        return f'student name:{self.name},major:{self.major},code portfolio score:{self.code_portfolio_score},group project score:{self.group_project_score},self exam score:{self.exam_score}'

# Example
student1=Student('RYX','BMI',90,80,90)
print(student1.info_student())

