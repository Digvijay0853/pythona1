# # def demo(func):
# #     return func()  #hello()
# #
# #
# # def outer(func):
# #     def inner(*args,**kwargs):
# #         for i in range(3):
# #          print(func(*args,**kwargs))
# #     return inner
# # @outer
# # def hello():
# #     return ('in hello')
# # hello()
# # @outer
# # def add(a,b):
# #     return a+b
# # add(10,20)
#
#
# def outer_most(n):
#     def outer(func):
#         def inner(*args,**kwargs):
#             for i in range(n):
#                 func(*args,**kwargs)
#         return inner
#     return outer
#
# @outer_most(50)
# def demo():
#     print('in demo')
# # var1 = outer_most(5)
# # var2=var1(demo)
# # var2()
# demo()


class decorator:

    def __init__(self,func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('hello everyone')
        self.func()


@decorator
def demo():
    print('in demo')

# var = decorator(demo)
# print(var())
demo()