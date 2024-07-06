# # # # # # class Animal:
# # # # # #     def __init__(self,name,color):
# # # # # #         self.name = name
# # # # # #         self.color = color
# # # # # #     def eat(self):
# # # # # #         return ('every animal need to eat')
# # # # # #
# # # # # #     def sleeping(self):
# # # # # #         return 'Every Animal sleeps'
# # # # # #
# # # # # # class Dog(Animal):
# # # # # #     def bark(self):
# # # # # #         return 'Dogs barks very much'
# # # # # #     def walk(self):
# # # # # #         return 'every dogs walks'
# # # # # #
# # # # # # class Goldenretriver(Dog):
# # # # # #     def human_freindly(self):
# # # # # #         return 'goldenretiver is human freindly'
# # # # # #
# # # # # # obj = Goldenretriver('PLUTO','WHITE')  #__INIT__()
# # # # # # print(obj.bark())
# # # # # # print(obj.eat())
# # # # # # print(obj.sleeping())
# # # # #
# # # # # '''
# # # # # hirarchical inheritance
# # # # # '''
# # # #
# # # #
# # # # class Employee:
# # # #     def __init__(self,id,name,sal):
# # # #         self.name = name
# # # #         self.id = id
# # # #         self.sal = sal
# # # #     def working(self):
# # # #         return 'Every work hard for the company'
# # # # class Developer(Employee):
# # # #
# # # #     def __init__(self,prog,id,name,sal):
# # # #         super().__init__(id,name,sal)
# # # #         self.programing_language = prog
# # # #     def developing(self):
# # # #         return (f'Hello my name is {self.name} and '
# # # #                 f'i can develop a using {self.programing_language}')
# # # #
# # # #
# # # # obj1 = Developer('python',1,'mayur',50000)  #__init__()
# # # # obj2 = Developer('Front-end',2,'Gayatri',50000)
# # # #
# # # # class Manager(Employee):
# # # #
# # # #     def __init__(self,team_size,id,name,sal):
# # # #         super().__init__(id,name,sal)
# # # #         self.team_size = team_size
# # # #     def management(self):
# # # #         return (f'Hello my name is {self.name} and i manage '
# # # #                 f'the team of {self.team_size} employees')
# # # # obj  =Manager(10,12,'Sharadha',100000)
# class Parent2:
#     def __init__(self):
#         print('in parent 2 class ')
# 
# class Parent1:
# 
#     def __init__(self):
#         print('in parent 1 class')
#         s1 = super()
#         s1.__init__()
#         print('parent 1 execution done ')
# class Child(Parent1,Parent2):
#     def __init__(self):
#         print('in child class')
#         s = super()
#         s.__init__()
#         print('child execution done')
# obj = Child()
# # 
# # class Flamable:
# #
# #     def __init__(self,methane):
# #         self.methane = methane
# #
# #     def burning(self):
# #         return  'evert flamable luquid burns '
# #
# # class Liquid:
# #
# #     def __init__(self,density,meth):
# #         self.density = density
# #         super().__init__(meth)
# #
# #
# #     def unshapable(self):
# #         return 'All liquids does not have shape'
# #
# # class fuel(Liquid,Flamable):
# #
# #     def __init__(self,fuel_type,price,density,meth):
# #         self.fuel_type = fuel_type
# #         self.price = price
# #         super().__init__(density,meth)
# #
# #     def vapourized(self):
# #         return 'When water comes in contact of air it will vapourized'
# #
# # obj = fuel('Petrol',100,85,'50%')
# # obj2 = fuel('diesel',95,75,'70%')
# class Grand_Parent:
#
#     def __init__(self):
#         print('in grand parent class constructor')
#
# class Parent1(Grand_Parent):
#
#     def __init__(self):
#         print('in parent 1 class constructor')
#         super().__init__()
#
# class Parent2(Grand_Parent):
#
#     def __init__(self):
#         print('in parent 2 class constructor')
#         super().__init__()
# class Child(Parent1,Parent2):
#
#     def __init__(self):
#         print('in child class Constructor')
#         super().__init__()
# obj = Child()


class Duck:

    def talk(self):
        print('Quack,Quack...')

class Dog:

    def talk(self):
        print('wolf wolf....')

def quack(object):
    if hasattr(object,'quack'):
        if callable(object.quack):
            object.quack()
    else:
        print('To quack the object should be duck type')
def speak(object):
    object.talk()
d = Duck()
m = Dog()
quack(d)
speak(m)





















