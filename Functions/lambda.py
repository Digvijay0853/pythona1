# # # # var=lambda a=10,b=12 : a+b
# # # # # print(var(1,2))
# # # #
# # # #
# # # #
# # # # # Write a function to return a list by reversing the item of a list if the
# # # # # item is of odd length string otherwise keeping the item as it is !.
# # # # names = ['apple', 'google', 'yahoo', 'facebook', 'yelp', 'flipkart',
# # # #          'gmail', 'instagram', 'microsoft']
# # # # def reverse_list_element(list):
# # # #     for i in range(len(list)):
# # # #         element = list[i]
# # # #         if len(element) % 2 != 0:
# # # #             list.pop(i)
# # # #             list.insert(i,element[::-1])
# # # #     return list
# # # #
# # # # # print(reverse_list_element(names))
# # # #
# # # # def reverse_list(list):
# # # #     index = 0
# # # #     end_value = len(list) -1
# # # #     while index <= end_value //2:
# # # #         list[index],list[end_value-index] = list[end_value-index],list[index]
# # # #         index+=1
# # # #     return list
# # # #
# # # # li=['hello',98,12,51,'bye','hii']
# # # # print(reverse_list(li))
# # #
# # #
# # #
# # # # ''''Pattern''''
# # #
# # # # end_value=int(input('Please enter the number of rows you want'))
# # # # for i in range(1,end_value+1):
# # # #     for j in range(i):
# # # #         print('*',end=' ')
# # # #     print()
# # #
# # # end_value=int(input('Please enter the number of rows you want'))
# # # for i in range(1,end_value+1):
# # #     for j in range(end_value+1-i):
# # #         print('*',end=' ')
# # #     print()
# #
# # for i in range(1,6):
# #     for j in range(6-i-1):
# #         print(' ',end=' ')
# #     for k in range(i):
# #         print('*',end=' ')
# #     print()
# #
# # add=lambda a,b:a+b
# # print(add(1,2))
#
# def reverse_words(senetnce):
#     l= senetnce.split()
#     reversed_sentence =' '.join(reversed(l))
#     return reversed_sentence
#
# print(reverse_words('hello everyone how are you'))

