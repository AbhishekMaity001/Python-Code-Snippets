# Static methods #2
class Person(object):
    population = 3445

    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country
    @classmethod  # class method will take an default parameter ie...class itself and it is always passed when we call this method
    def showAll(self):
        print('Name is %s, age is : %s , country is : %s' %(self.name, self.age, self.population))

    @staticmethod  # it can be called without the self also bcoz it dont pass the class instance by default
    def checkpop():
        return  18

if __name__=='__main__':
    per = Person('Abhishek maity', 18, 'India')
    per.showAll()
    print(Person.checkpop())
    print(help(Person))