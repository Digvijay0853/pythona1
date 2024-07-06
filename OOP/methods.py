# # # # # # # class Sample:
# # # # # # #
# # # # # # #     def __init__(self,a,b):
# # # # # # #         self.a =a
# # # # # # #         self.b = b
# # # # # # #     def values(self):
# # # # # # #         return self.a + self.b
# # # # # # #
# # # # # # # obj1 = Sample(1,2)
# # # # # # # obj2 = Sample(3,4)
# # # # # # # print(obj1.values())
# # # # # # # print(obj2.values())
# # # # # # #
# # # # # #
# # # # # # class Sample:
# # # # # #
# # # # # #     a = 10
# # # # # #     b = 20
# # # # # #     @classmethod
# # # # # #     def details(cls):
# # # # # #         return cls.a + cls.b
# # # # # # print(Sample.details())
# # # # # #
# # # # # #
# # # # # # class Sample:
# # # # # #
# # # # # #     a = 10
# # # # # #     b = 20
# # # # # #     def __init__(self):
# # # # # #         self.a = 100
# # # # # #     @classmethod
# # # # # #     def details(cls):
# # # # # #         return cls.a + cls.b
# # # # # #
# # # # # #     def sub(self):
# # # # # #         return self.a-self.b
# # # # # # obj = Sample()
# # # # # # print(Sample.__dict__)
# # # # # # # print(obj.details())
# # # # #
# # # # #
# # # # # class Sample:
# # # # #
# # # # #     a = 10
# # # # #     b = 20
# # # # #
# # # # #     def __init__(self,c,d):
# # # # #         self.c = c
# # # # #         self.d = d
# # # # #     @staticmethod
# # # # #     def demo():
# # # # #         print('hello')
# # # # # obj = Sample(30,40)
# # # # # # Sample.demo()
# # # # # # obj.demo()
# # # #
# # # class Student:
# # #     collage_name = 'xyz'
# # #     def __init__(self,name,email,number):
# # #         self.name = name
# # #         self.email = email
# # #         self.number= number
# # #
# # #     def details(self):
# # #         return (f'Hello my name is {self.name} and mo no is {self.number}'
# # #                 f'and my collage name is {self.collage_name}')
# # #
# # # obj1 = Student('Tony','tony@123',12345698)
# # # obj2 = Student('Steve','Steve@123',12345698)
# # # print(obj1.details())
# # # print(obj2.details())
# #
# # class Sample:
# #     __a=10
# #     __b=20
# #
# #     def __init__(self,c,d):
# #         self.c = c
# #         self.d = d
# #     def add(self):
# #
# #
# # print(Sample.__dict__)
#
# class Sample:
#
#      __a = 10
#      __b = 20
#
#      def __init__(self):
#          self.__c = 40
#
#
#
#
# # print(Sample.__a)
# obj =Sample()
# print(obj.__c)
