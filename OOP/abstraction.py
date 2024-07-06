from abc import ABC,abstractmethod
class Parent(ABC):
    @abstractmethod
    def eat_sweets(self):
        pass

class Child(Parent):

    def eat_sweets(self):
        print('i like sweets ')
obj = Child()
obj.eat_sweets()