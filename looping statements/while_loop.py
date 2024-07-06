# # # # # index=0
# # # # # # s=input('Enter the string : ')
# # # # # # while index <= len(s)-1:
# # # # # #     print(s[index])
# # # # # #     index+=1
# # # # # # l=[1,2,3,4,5,6,7,8,9,10]
# # # # # # index=0
# # # # # # while index < len(l):
# # # # # #     num=l[index]#l[1]    num=2
# # # # # #     if num % 2 == 1:
# # # # # #         print(num)
# # # # # #     index+=1
# # # # #
# # # # #
# # # # # # s='digvijay'
# # # # # # index=0lll
# # # # # # count=0
# # # # # # while index < len(s):
# # # # # #     char=s[index]
# # # # # #     if char in 'aieouAIEOU':
# # # # # #         count+=1
# # # # # #     index+=1
# # # # # # print(count)
# # # # # l=['aa','raju','maar','sale','ko','maar']  #244424
# # # # # index=0
# # # # # while index <= 5:
# # # # #     ele=l[index]
# # # # #     print(f'The length of the word {ele} is {len(ele)}')
# # # # #     index+=1
# # # #
# # # # # char=input('Enter the character : ')
# # # # # if len(char) == 1:
# # # # #     if char in 'aieouAIEOU':
# # # # #         d={}
# # # # #         d[char] = ord(char)
# # # # #         print(d)
# # # # #     else:
# # # # #         print('Entered character is not a vowel')
# # # # # else:
# # # # #     print('Entered single value only')
# # # #
# # # # dev_team={'Name' : 'Raju','sal':150,'Job':'Developer'}
# # # # # if 'sall' in dev_team.keys():
# # # # #     dev_team['sal'] += 1
# # # # #     print(dev_team)
# # # # # else:
# # # # #     print(dev_team)
# # # # # if len(dev_team.keys()) % 2 == 0:
# # # # #     print(dev_team)
# # # # # else:
# # # # #     dev_team['comm'] = 500
# # # # #     print(dev_team)
# # # # number=int(input("Enter the Number : "))
# # # # num=str(number)
# # # # first=int(num[0])
# # # # second_last=int(num[-2])
# #
# # '''Palindrome string'''
# # s=input('Enter the String :')
# # new_string=''
# # index = len(s)-1
# # while index >= 0:
# # 	char=s[index]
# # 	new_string+=char
# # 	index-=1
# # print(new_string)
# #
# # if s == new_string:
# # 	print(s+' is a palindrome string')
# # else:
# # 	print(s+' is not a palindrome string')
#
#
# s='hello everyone how are you'
# list=s.split()  #['hello', 'everyone', 'how', 'are', 'you']
# new_list=[]
# index=0
# while index <= len(list)-1:
# 	ele=list[index]
# 	new_list.append(len(ele))
# 	index+=1
# new_list.sort()
# largest=new_list[-1]
# num=0
# while num <= len(list)-1:
# 	ele=list[num]
# 	if largest == len(ele):
# 		print('The largest word present in the string is '+ele)
# 	num+=1




from threading import *



