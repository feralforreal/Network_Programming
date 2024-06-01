#!usr/bin/env python3

from datetime import date

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    @classmethod
    def fromBirthYaer(cls, name, year):
        return cls(name, date.today().year - year)

    @staticmethod
    def isAdult(age):
        return age > 18
    
person1 = Person('mayank', 21)
person2 = Person.fromBirthYaer('mayank', 1996)

print(person1.age)
print(person2.age)

print(Person.isAdult(27))