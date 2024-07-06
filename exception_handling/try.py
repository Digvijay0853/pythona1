# # s='hello'
# # for i in range(6):
# #     try:
# #        print(s[i])
# #     finally:
# #         print('in finally')
#
# def div(a,b):
#     try:
#         a//b
#     finally:
#         print('in finally')
# # div(1,0)
#
# def div(a,b):
#     try:
#         a//b
#     except BaseException:
#         print('error handled')
#     finally:
#         print('in finally')
# div(1,0)
class Negative_value_exception(BaseException):
    pass
def sub(a,b):
    if b > a :
        raise Negative_value_exception('negative value output')
    else:
        return a-b
print(sub(1,3))