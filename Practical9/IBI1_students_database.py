name=input('please input student name:')
major=input('please input student major BMS or BMI:')
code_portfolio_score=input('please input student code portfolio score:')
group_project_score=input('please input student group project score:')
exam_score=input('please input student exam score:')
#collect the student information
class Student:
    def  __init__(self,name,major,code_portfolio_score,group_project_score,exam_score):
        self.name = name
        self.major = major
        self.code_portfolio_score = code_portfolio_score
        self.group_project_score = group_project_score
        self.exam_score =exam_score
    #try to define a function that can collect the student information
    def print_student(self):
        print(f'student name:{self.name},major:{self.major},code portfolio score:{self.code_portfolio_score},group project score:{self.group_project_score},self exam score:{self.exam_score}')
student1=Student(name=name,major=major,code_portfolio_score=code_portfolio_score,group_project_score=group_project_score,exam_score=exam_score)
student1.print_student()