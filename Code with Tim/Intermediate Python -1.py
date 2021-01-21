# optional parameters

# def func(word, frequency=10) :
#     return word*frequency
#
# call = func('Abhishek',20)
# print(call)

class Employee():
    def __init__(self, empid, name, age, department, salary=600000):
        self.empid = empid
        self.name = name
        self.age = age
        self.department = department
        self.salary = salary

    def showAll(self, display=True):
        if display==True:
            print('employee id : %s , empname = %s, age = %s, department = %s, salary = %s'%(self.empid, self.name, self.age, self.department, self.salary))
        else :
            print('He is a Data Scientist at %s department'%self.department)

if __name__ == '__main__' :
    emp = Employee(123, 'Abhishek', 23, 'Computer Science')
    emp.showAll(True)







