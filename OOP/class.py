# class Sample:
#
#     a=100
#     def __init__(self,c,d):
#         self.a = c
#
# obj = Sample(10,20)
# print(obj.a)
#
# class Sample:
#
#     a=100
#     def __init__(self,c,d):
#         self.c = c
#
# obj = Sample(10,20)

class Sample :
    a=100
    b=100

    def __init__(self,c,d):
        self.c = c
        self.d = d
obj1 = Sample(10,20)
obj2 = Sample(30,40)
obj3 = Sample(60,70)
print(obj1.c)
print(obj2.c)
print(obj3.c)

