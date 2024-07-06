# # # # a='hello'
# # # # # print(len(a))
# # # # # # print(a.count('l'))
# # # #
# # # # def demo():
# # # #     return 'demo'
# # # # print(demo())
# # # #
# # #
# # # def add(a,b):
# # #     return a+b
# # #
# # # print(add(10,20))
# # #
# # # def add(c,d,a=10,b=20):
# # #     return a+b+c+d
# # # # print(add(b=23))
# # # print(add(1,2,3,4))
# #
# # def employee(ename,email,company_name = 'Google'):
# #     return (f'my name is {ename} and my email is {email} and '
# #             f'company name is {company_name}')
# #
# # # print(employee('mayur','mayur@123'))
# #
# # def func(*a):
# #     a,b,c,d,e =  a
# #     print(a)
# #
# # print(func(1,2,3,4,5))
# #
# # def add(*a):
# #     for i in a:
# #         print(i)
# # add(1,2,3,4,5,6,85)
#
#
# def func(**a):
#     e,b,*c,d= a
#     print(a[e])
#     print(a[b])
#     print(a[c])
# # func(a=1,b=2,c=3,d=4)
#
#
#
# def func(**a):
#     for i in a:
#         print(i)
# # func(a=1,b=2,c=3,d=4)
#
#
def func(**a):
    a,*b=a
    print(b)
    print(a)
# print(func(a=12,b=13,c=14,d=15))
'''
methods Recursion
'''
# def demo(a):
#     print('in demo')
#     if a <= 10:
#        a+=1
#        demo(a)
# demo(5)


