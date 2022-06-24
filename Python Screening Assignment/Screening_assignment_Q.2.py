# 2.Demonstrate use of abstract class, multiple inheritance and decorator in python using examples.
from abc import ABC, abstractmethod

class Calculator(ABC): # Inheritance and making Calculator class as an abstract class

    @abstractmethod       # Decorator
    def addition(self):
        pass

    @abstractmethod       # Decorator
    def multiplication(self):
        pass


class Calci(Calculator): # Multiple inheritance (Calculator class inherit abstract class ABC and Calci class inherit Calculator class)
    def __init__(self,number1, number2):
        self.number1 = number1
        self.number2 = number2

    def addition(self):
        summ = self.number1 + self.number2
        return summ

    def multiplication(self):
        productt = self.number1 * self.number2
        return productt

cal = Calci(5,8)
cal1 = cal.addition()
cal2 = cal.multiplication()

print(cal1)
print(cal2)







