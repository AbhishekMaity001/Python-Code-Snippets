# Static methods #2
class Person(object):
    population = 3445

    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

    def showAll(self):
        print('Name is %s, age is : %s , country is : %s' %(self.name, self.age, self.country))


    def checkpop(self,age):
        return age >= 18

if __name__=='__main__':
    per = Person('Abhishek maity', 18, 'India')
    per.showAll()
    print(per.checkpop(20))