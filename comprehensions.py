# # l =set()
# # for i in range(1,11):
# #     if i % 2 == 0:
# #         l.add(i)
# #
# # l1 = {i for i in range(1,11) if i % 2 == 0}
# # print(l)
# # print(l1)
# #
# # string = input('enter the string')
# # l=set()
# # for i in string:
# #     if i in 'AIEOUaieou':
# #         l.add(i)
# # l2 = {i for i in string if i in 'AIOEUaieou'}
# # print(l2)
# # print(l)
# #
# #
# # l = ['mayur','pooja','nilam','kartik','satyam']
# # l1=set()
# # for i in l:
# #     if len(i) % 2 == 0:
# #         l1.add(i)
# #     else:
# #         l1.add(i[::-1])
# #
# # l2 = {i if len(i) % 2 ==0 else i[::-1] for i in l}
# # print(l1)
# # print(l2)
#
# d={}
# s='hello'
# for i in s:
#     d[i] = ord(i)
# print(d)
#
# d1 = {i:ord(i) for  i in s}
# print(d1)